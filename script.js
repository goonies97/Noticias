import { config } from "dotenv"
config()

import { Configuration, OpenAIApi} from "openai"
import readline from "readline"

//Llama API
const openai =new OpenAIApi (new Configuration({
    apiKey: process.env.API_KEY
}))

// Crea interfaz
const userInterface = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

// Crea un arreglo vacío para almacenar el historial de chat
const chatHistory = []

//Configuración e interacción de ChatGPT
userInterface.prompt()
userInterface.on("line", async input => {

    const message = { role: "user", content: input }
    
    // Agrega el mensaje actual al historial de chat
    chatHistory.push(message)
    
    const res = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        n: 1,
        max_tokens: 150,
        
        // Envía todo el historial de chat al modelo de OpenAI
        messages: chatHistory
        
    })
    console.log(res.data.choices[0].message.content)
    userInterface.prompt()
})
