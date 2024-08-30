import streamlit as st
st.title("Chain of thought few shot Model Page")
st.markdown('''Here, we utilise a :red[Chain-of-Thought (CoT)] prompting framework that allows us to make our LLM reason through its response before returning an output.\
As outlined in the landmark paper on CoT prompting ([Wei et. al., Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/pdf/2201.11903)), CoT prompting allows LLMs to look at a few examples (i.e. few-shot prompting) and the thought process behind them. The paper studies several LLMs on several different models such as PaLM and LaMDA, as well as GPT-3.\
In the paper above, CoT prompting serves to:
  - Debug any visual hallucinations by asking the model to describe the image
  - Provide examples of certain characteristics/telltale features of the diseases for the LLM to look out for

However, CoT prompting do show two major downsides compared to zero-shot prompting, namely:
  - More tokens are passed into the LLM, hence we reached the token limit of our API key fairly quickly (due to this we were unable to gather enough test results to plot a full confusion matrix)
  - More complex to implement

We implemented CoT prompting as such:
***''')

message = [
    {'role': 'system',
        'content': """You are a medical student. You will be given several retinal fundus images as a test.
Firstly, describe key features depicted in the image, of no less than 100 words, such as the macula, optic nerve, optic cup and disc and retinal blood discs.
If the eye is healthy, say \"HEALTHY\". If not, tell me whether the patient has \"CATARACT\", \"DIABETIC RETINOPATHY\", or \"GLAUCOMA\". Your final diagnosis must be strictly 1 or 2 words, on a new line."""
    },
    {"role": "user",
        "content": [
            {"type": "text", "text": "Produce a diagnosis for the following:"},
            {"type": "image_url", "image_url": {
                "url": "https://github.com/SIC-AR112-2024/SICAR112-Eye-Diesease-Prediction/blob/main/dataset/diabetic_retinopathy/342.jpg?raw=true",
            },
            },
        ],
    },
    {"role": "assistant",
    "content": """The fundus image shows numerous hard exudates scattered throughout the retina, particularly in the macula. These are yellowish-white deposits that are a hallmark of diabetic retinopathy. Additionally, there are microaneurysms, which are small, dilated blood vessels that leak fluid. These features, along with the presence of retinal hemorrhages, are consistent with diabetic retinopathy. The optic nerve appears healthy, ruling out glaucoma. There is no evidence of a cataract.
DIABETIC RETINOPATHY."""
    },
    {"role": "user",
        "content": [
            {"type": "text", "text": "Produce a diagnosis for the following:"},
            {"type": "image_url", "image_url": {
                "url": "https://github.com/SIC-AR112-2024/SICAR112-Eye-Diesease-Prediction/blob/main/dataset/glaucoma/883.jpg?raw=true",
            },
            },
        ],
    },
    {"role": "assistant",
    "content": """The image shows a view of the fundus of the eye. The optic disc, the point where the optic nerve leaves the eye, is visible in the center of the image. The disc is slightly pale and the margins appear blurred. The macula, the central region responsible for central vision, appears slightly edematous. The retinal blood vessels are clearly visible and appear normal.
GLAUCOMA"""}]
message.append({"role": "PROMPT",
            "content": [
                {"type": "text", "text": "Produce a diagnosis for the following:"},
                {"type": "image_url", "image_url": {
                    "url": "https://github.com/SIC-AR112-2024/SICAR112-Eye-Diesease-Prediction/blob/main/dataset/diabetic_retinopathy/1025.jpg?raw=true"
}}]})
for i in message:
    if i['role'] == 'user':
        with st.chat_message('user'):
            st.write(i['content'][0]['text'])
            st.image(i['content'][1]['image_url']['url'])
    elif i['role'] == 'system':
        with st.chat_message('System Instructions', avatar = ':material/computer:'):
            st.write(i['content'])
    elif i['role'] == 'PROMPT':
        with st.chat_message('USER PROMPT', avatar = '❓'):
            st.write(i['content'][0]['text'])
            st.image(i['content'][1]['image_url']['url'])
    else:
        with st.chat_message('ai'):
            st.write(i['content'])