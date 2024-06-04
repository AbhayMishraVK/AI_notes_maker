from typing import List
from langgraph.graph import END, StateGraph
from typing_extensions import TypedDict
from graph_nodes import *
import streamlit as st


class GraphState(TypedDict):
    user_question: str
    youtube_video_present: bool
    list_of_url: List
    list_of_question: List
    current_question: str
    summary_of_video: str
    example: str
    real_life_example: str
    advantage_and_disadvantage: str
    definition: str
    difference: str
    types: str
    reason: str


def check_answer_type(state):
    list_of_url = state['list_of_url']
    if len(list_of_url) > 0:
        return 'continue'
    else:
        return 'stop'


def graph_nodes(workflow):
    workflow.set_entry_point("starting_node")
    workflow.add_node("starting_node", starting_node)
    workflow.add_node("take_url_and_make_summary_node", take_url_and_make_summary_node)
    workflow.add_node("create_intro_definition_node", create_intro_definition_node)
    workflow.add_node("create_advantage_and_disadvantage", create_advantage_disadvantage_node)
    workflow.add_node("create_reason_node", create_reason_node)
    workflow.add_node("create_difference_node", create_difference_node)
    workflow.add_node("create_types_node", create_types_node)
    workflow.add_node("create_example_node", create_example_node)
    workflow.add_node("create_real_life_example_node", create_real_life_example_node)
    workflow.add_node("append_notes_in_docx_nodes", append_notes_in_docx_node)
    return workflow


def graph_flow(workflow):
    workflow.add_edge("starting_node", "take_url_and_make_summary_node")
    workflow.add_edge("take_url_and_make_summary_node", "create_intro_definition_node")
    workflow.add_edge("create_intro_definition_node", "create_advantage_and_disadvantage")
    workflow.add_edge("create_advantage_and_disadvantage", "create_reason_node")
    workflow.add_edge("create_reason_node", "create_types_node")
    workflow.add_edge("create_types_node", "create_difference_node")
    workflow.add_edge("create_difference_node", "create_example_node")
    workflow.add_edge("create_example_node", "create_real_life_example_node")
    workflow.add_edge("create_real_life_example_node", "append_notes_in_docx_nodes")
    workflow.add_conditional_edges("append_notes_in_docx_nodes", check_answer_type, {
        'continue': 'take_url_and_make_summary_node',
        'stop': END
    })
    return workflow


workflow = StateGraph(GraphState)
workflow = graph_nodes(workflow)
workflow = graph_flow(workflow)
final_graph_for_videos = workflow.compile()