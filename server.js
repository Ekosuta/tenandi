const express = require('express');
const app = express();
const mongoose = require('mongoose')

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

mongoose.connect('mongodb://localhost:27017/tenandi', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('connected to MongoDB'))
.catch(err => console.error('failed to connec to MongoDB:', err));

app.get('/', (req, res) => {
    res.send('hello world')
})

const PORT = 3001;
app.listen(PORT, () => {
    console.log(`The server is running on port ${PORT}`)
})