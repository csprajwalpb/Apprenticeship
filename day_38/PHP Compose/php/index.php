<?php
// Database configuration
$host = $_ENV['MYSQL_HOST'] ?? 'localhost';
$port = $_ENV['MYSQL_PORT'] ?? '3306';
$dbname = $_ENV['MYSQL_DATABASE'] ?? 'phpdb';
$username = $_ENV['MYSQL_USER'] ?? 'phpuser';
$password = $_ENV['MYSQL_PASSWORD'] ?? 'phppass';

try {
    $pdo = new PDO("mysql:host=$host;port=$port;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// Handle API requests
$method = $_SERVER['REQUEST_METHOD'];
$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($method === 'OPTIONS') {
    http_response_code(200);
    exit();
}

// Create users table if it doesn't exist
$pdo->exec("CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)");

switch ($method) {
    case 'GET':
        if ($path === '/api/users' || $path === '/api/users/') {
            $stmt = $pdo->query("SELECT * FROM users ORDER BY created_at DESC");
            $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
            echo json_encode($users);
        } elseif (preg_match('/\/api\/users\/(\d+)/', $path, $matches)) {
            $id = $matches[1];
            $stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
            $stmt->execute([$id]);
            $user = $stmt->fetch(PDO::FETCH_ASSOC);
            if ($user) {
                echo json_encode($user);
            } else {
                http_response_code(404);
                echo json_encode(['error' => 'User not found']);
            }
        } elseif ($path === '/api/health' || $path === '/api/health/') {
            echo json_encode(['status' => 'OK', 'message' => 'PHP application is running!']);
        } else {
            // Serve the main page
            ?>
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>PHP Docker App</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
                    .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                    h1 { color: #333; text-align: center; }
                    .api-section { margin: 20px 0; padding: 20px; background: #f8f9fa; border-radius: 5px; }
                    .endpoint { background: #e9ecef; padding: 10px; margin: 10px 0; border-radius: 3px; font-family: monospace; }
                    .method { color: #28a745; font-weight: bold; }
                    .url { color: #007bff; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🐘 PHP Docker Application</h1>
                    <p>Welcome to the PHP application running in Docker!</p>
                    
                    <div class="api-section">
                        <h3>Available API Endpoints:</h3>
                        <div class="endpoint"><span class="method">GET</span> <span class="url">/api/users</span> - Get all users</div>
                        <div class="endpoint"><span class="method">GET</span> <span class="url">/api/users/{id}</span> - Get user by ID</div>
                        <div class="endpoint"><span class="method">POST</span> <span class="url">/api/users</span> - Create new user</div>
                        <div class="endpoint"><span class="method">PUT</span> <span class="url">/api/users/{id}</span> - Update user</div>
                        <div class="endpoint"><span class="method">DELETE</span> <span class="url">/api/users/{id}</span> - Delete user</div>
                        <div class="endpoint"><span class="method">GET</span> <span class="url">/api/health</span> - Health check</div>
                    </div>
                    
                    <div class="api-section">
                        <h3>Database Status:</h3>
                        <?php
                        try {
                            $stmt = $pdo->query("SELECT COUNT(*) as count FROM users");
                            $result = $stmt->fetch(PDO::FETCH_ASSOC);
                            echo "<p>✅ Connected to MySQL database</p>";
                            echo "<p>Total users in database: " . $result['count'] . "</p>";
                        } catch (Exception $e) {
                            echo "<p>❌ Database connection error: " . $e->getMessage() . "</p>";
                        }
                        ?>
                    </div>
                </div>
            </body>
            </html>
            <?php
        }
        break;
        
    case 'POST':
        if ($path === '/api/users' || $path === '/api/users/') {
            $input = json_decode(file_get_contents('php://input'), true);
            if ($input && isset($input['name']) && isset($input['email'])) {
                try {
                    $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
                    $stmt->execute([$input['name'], $input['email']]);
                    $userId = $pdo->lastInsertId();
                    $stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
                    $stmt->execute([$userId]);
                    $user = $stmt->fetch(PDO::FETCH_ASSOC);
                    http_response_code(201);
                    echo json_encode($user);
                } catch (PDOException $e) {
                    http_response_code(400);
                    echo json_encode(['error' => 'Failed to create user: ' . $e->getMessage()]);
                }
            } else {
                http_response_code(400);
                echo json_encode(['error' => 'Invalid input data']);
            }
        }
        break;
        
    case 'PUT':
        if (preg_match('/\/api\/users\/(\d+)/', $path, $matches)) {
            $id = $matches[1];
            $input = json_decode(file_get_contents('php://input'), true);
            if ($input && isset($input['name']) && isset($input['email'])) {
                try {
                    $stmt = $pdo->prepare("UPDATE users SET name = ?, email = ? WHERE id = ?");
                    $stmt->execute([$input['name'], $input['email'], $id]);
                    if ($stmt->rowCount() > 0) {
                        $stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
                        $stmt->execute([$id]);
                        $user = $stmt->fetch(PDO::FETCH_ASSOC);
                        echo json_encode($user);
                    } else {
                        http_response_code(404);
                        echo json_encode(['error' => 'User not found']);
                    }
                } catch (PDOException $e) {
                    http_response_code(400);
                    echo json_encode(['error' => 'Failed to update user: ' . $e->getMessage()]);
                }
            } else {
                http_response_code(400);
                echo json_encode(['error' => 'Invalid input data']);
            }
        }
        break;
        
    case 'DELETE':
        if (preg_match('/\/api\/users\/(\d+)/', $path, $matches)) {
            $id = $matches[1];
            try {
                $stmt = $pdo->prepare("DELETE FROM users WHERE id = ?");
                $stmt->execute([$id]);
                if ($stmt->rowCount() > 0) {
                    http_response_code(200);
                    echo json_encode(['message' => 'User deleted successfully']);
                } else {
                    http_response_code(404);
                    echo json_encode(['error' => 'User not found']);
                }
            } catch (PDOException $e) {
                http_response_code(400);
                echo json_encode(['error' => 'Failed to delete user: ' . $e->getMessage()]);
            }
        }
        break;
        
    default:
        http_response_code(405);
        echo json_encode(['error' => 'Method not allowed']);
}
?>