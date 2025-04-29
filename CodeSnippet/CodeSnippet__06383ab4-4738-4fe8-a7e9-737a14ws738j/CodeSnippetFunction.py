from gaas_gpt_model import ModelEngine
def generate_response(description,insight_id,language="python"):
    if not language.isalpha():
        raise ValueError("Invalid language parameter")
    model = ModelEngine(engine_id = "4801422a-5c62-421e-a00c-05c6a9e15de8", insight_id=insight_id)
    question=f"Create a function in {language} that {description}" 
    try:
        output = model.ask(question=question)
    except Exception as e:
        raise ConnectionError(f"Model engine request failed: {e}")
    
    if isinstance(output, list) and len(output) > 0 and isinstance(output[0], dict) and 'response' in output[0] and isinstance(output[0]['response'], str):
        return f"```{language}\n{output[0]['response']}\n```"   
    else:        
        raise ValueError("Unexpected output format from model.ask()")
