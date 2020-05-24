# Ultimate-Covid-API
A API que deu certo.

# Passo a passo

* Crie um database no Postgres chamado 'ultimate-covid-api'
* Vá até o arquivo **settings.py** e substitua o campo 'user' e 'pwd' com as suas credenciais no Postgres
* Crie um ambiente virtual com o venv chamado 'myvenv' e instale as dependências encontradas no arquivo 'requirements.txt'
* Depois de entrar no ambiente virtual, rode o comando **python server.py**
* Após isso, acesse a url [http://127.0.0.1:5000](http://127.0.0.1:5000) e faça as requisições.

# Como fazer requisições em APIs GraphQL?

Do lado direito é possível ver as querys disponíveis para consulta. Escolhendo uma, é só colocar os parâmetros e atributos em formato de JSON e passá-las junto com a query na URL.

## Exemplo de requisição
A consulta aos casos de um determinado município se daria dessa forma:

 ### Pelo Postman:
 Adicione á url ( [http://127.0.0.1:5000/cases](http://127.0.0.1:5000/cases) ) a chave 'query', e nela passe o json com sua consulta.
 
Exemplo: 
[http://127.0.0.1:5000/cases?query={casesPerCity(city: "Sertãozinho",date:"", state:"PB") {casos,obitos,recuperados}}](http://127.0.0.1:5000/cases%20?query=%7B%20%09casesPerCity%28city:%20%22Sert%C3%A3ozinho%22,%20date:%22%22,%20state:%22PB%22%29%20%7B%20%09%09casos,%20%09%09obitos,%20%20%09%09recuperados%20%09%7D%20%09%20%7D)

>Meio grande né?   

### Pelo GraphiQL
Apenas coloque no campo de consulta o JSON com os dados que você quer recuperar.
Exemplo:

    {
    	casesPerCity(date:"2020-05-20", city:"Sertãozinho", state:"PB") {
	    		regiao,
    		casos,
    		obitos
    	}
    }

# Posso ajudar?
Como esse é um projeto para aprender a desenvolver APIs com GraphQL, ainda há muita coisa a ser implementada. Caso ache algum erro ou sugestão de melhoria no código, sinta-se a vontade para criar uma issue ou pode entrar em contato comigo através do email ana.paula@dcx.ufpb.br.
