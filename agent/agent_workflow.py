authors=["Sabarno Pramanick"]

from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessageState, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from tools.weather_info import WeatherInfoTool
from tools.place_search import PlaceSearchTool
from tools.calculator import CalculatorTool
from tools.currency_conversion import CurrencyConverterTool


class GraphBuilder():
    def __init__(self,model_provider: str = "groq"):
        self.model_loader= ModelLoader(model_provider=model_provider)
        self.llm= self.model_loader.load_llm()
        self.tools=[]
        self.weather_tools= WeatherInfoTool()
        self.place_search_tools= PlaceSearchTool()
        self.calculator_tools= CalculatorTool()
        self.currrency_converter_tools= CurrencyConverterTool()
        self.tools.extend([
            * self.weaather_tools.weather_tool_list,
            * self.place_search_tools.place_search_tool_list,
            * self.calculator_tools.calculator_tool_list,
            * self.currrency_converter_tools.currency_converter_tool_list
        ])
        self.llm_with_tools= self.llm.bind_tools(tools=self.tools)
        self.graph=None
        self.system_prompt= SYSTEM_PROMPT
    
    def agent_function(self,state:MessageState):
        """ Main function to build the agent workflow. """
        
        user_question=state["message"]
        input_question=[self.system_prompt]+ user_question
        response=self.llm_with_tools.invoke(input_question)
        return {'messages':[response]}


    def build_graph(self):
        graph_builder= StateGraph(MessageState)
        graph_builder.add_node("Agent", self.agent_function)
        graph_builder.add_node("Tools", ToolNode(tools=self.tools))
        graph_builder.add_edge(START, "Agent")
        graph_builder.add_conditional_edges("Agent",tools_condition)
        graph_builder.add_edge("Tools", "Agent")
        graph_builder.add_edge("Agent",END)
        self.graph=graph_builder.compile()
        return self.graph

    def __call__(self):
        return self.build_graph()
