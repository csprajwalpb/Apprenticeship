const express = require('express');
const app = express();

app.use(express.json());

// Sample routes
app.get('/', (req, res) => {
  res.json({ message: "🚀 Node.js Docker Application", version: "1.0.0" });
});

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', uptime: process.uptime() });
});

app.get('/api/users', (req, res) => {
  res.json([{ id: 1, name: "Alice" }, { id: 2, name: "Bob" }]);
});

app.get('/api/users/:id', (req, res) => {
  const id = parseInt(req.params.id);
  res.json({ id, name: id === 1 ? "Alice" : "Bob" });
});

app.post('/api/users', (req, res) => {
  const user = req.body;
  res.status(201).json({ message: "User created", user });
});

app.put('/api/users/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const user = req.body;
  res.json({ message: `User ${id} updated`, user });
});

app.delete('/api/users/:id', (req, res) => {
  const id = parseInt(req.params.id);
  res.json({ message: `User ${id} deleted` });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
