const express = require('express');
const app = express();
const cors = require('cors');



app.use(express.urlencoded({extended:false}));
app.use(express.json());
app.use(cors());

app.get('/', (req,res)=>{
    console.log(req);
    res.send('hola');
})

app.listen(3000,()=>{
    console.log("funcionando");
})