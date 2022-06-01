const express = require('express');
const exphbs = require('express-handlebars');

const app = express();
const post = process.enc.PORT || 5000;


app.engine('hbs, exphbs({extname: *.hbs'}));
app.set('view engine', 'hbs');


app.listen(port, ()=> console.log(Listening on port ${port}));
