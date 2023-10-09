import openai

#Chave da API 
openai.api_key = 'APIKEY' 

regras_resposta = [ 
    {'role': 'system', 'content': 'Você será um melhorador de descrições de um site onde pessoas anunciam seus produtos'},
    {'role': 'system', 'content': 'Responda sempre de maneira mais longa e detalhada que conseguir'}, 
    {'role': 'system', 'content': 'Não use abreviações'}
    ] 

def obter_query(pergunta,regra_inicial):
    prompt = 'Pergunta: ' + pergunta + '\n\nRegras:\n' + '\n'.join([f"{item['role']}: {item['content']}" for item in regra_inicial]) 
    response = openai.Completion.create( engine='text-davinci-003', prompt=prompt, max_tokens=200, n=1, stop=None, temperature=0.2, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0 ) 
    output = response.choices[0].text.strip().split('Resposta: ') 
    resposta = output[0] 

    if len(output) > 1: 
        consulta_split = output[0].split('Regras de Consulta:') 
        resposta = output[1] 

    return resposta 

# Pergunta do usuário 
pergunta_usuario = "ps2 bom, controle sem analógico e com memory card" 
resposta_chatgpt = obter_query(pergunta_usuario,regras_resposta)

print('Resposta do ChatGPT:', resposta_chatgpt)
