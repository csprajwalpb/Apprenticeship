const express = require('express');
const bodyParser = require('body-parser');
const tutorialsRouter = require('./routes/tutorials');
const connectDB = require('./db');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());

connectDB();

app.use('/api/tutorials', tutorialsRouter);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});