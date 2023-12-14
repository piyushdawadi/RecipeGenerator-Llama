import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function To get response from Llama2 model

def getLLamaresponse(food_name,cuisine):

    ### LLama2 model
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':512,
                              'temperature':0.1})
    
    ## Prompt Template

    template="""
        Write a recipe for {cuisine} cuisine for the food {food_name}. 
        First list the ingredients in points format not in paragraph style, and then list the procedure to make it step by step in points format not in paragraph style.
        Make sure to fit all these within the speocfied max_new_token parameters.
            """
    
    prompt=PromptTemplate(input_variables=["cuisine","food_name"],
                          template=template)
    
    ## Generate the response from the LLama 2 model
    response=llm(prompt.format(cuisine=cuisine,food_name=food_name))
    print(response)
    return response






st.set_page_config(page_title="Recepe Generator",
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Recipe Generator")

## creating two more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    cuisine=st.text_input('Cuisine')
with col2:
    food_name=st.text_input('Food Name')
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(food_name,cuisine))