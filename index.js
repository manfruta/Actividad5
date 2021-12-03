const express = require('express');
const app = express();
const cors = require('cors');
const { Client } = require('pg')


app.use(express.urlencoded({extended:false}));
app.use(express.json());
app.use(cors());

app.get('/', (req,res)=>{
    console.log(req);
    res.send('hola');
})

const client = new Client({
    connectionString: process.env.DATABASE_URL, //
    ssl: {rejectUnauthorized: false}
  })
  
  

  app.get('/tabla', (req,res)=>{
    let datos = {}
    client.connect()

    client.query('SELECT * from criptomarze', (err, res) => {
       // console.log(err, res)
        console.log(re.Result.rows)
        datos = res.json()
        client.end()
    })
    res.send(datos)
})

app.listen(process.env.PORT,()=>{
    console.log("funcionandooooooo");
})
