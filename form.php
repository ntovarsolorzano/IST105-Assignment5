<!DOCTYPE html>
<html>
<head>
    <title>Treasure Hunt</title>
</head>
<body>
    <h1>Interactive Treasure Hunt</h1>

    <form method="post">  <!-- Removed action attribute -->
        <label for="number">Enter a Number (e.g., Birth Year):</label><br>
        <input type="number" id="number" name="number" required><br><br>

        <label for="text">Enter a Text Message (e.g., Name or Secret Word):</label><br>
        <input type="text" id="text" name="text" required><br><br>

        <input type="submit" value="Solve the Puzzle">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Retrieve and sanitize user input (very important!)
        $number = escapeshellarg($_POST['number']);
        $text = escapeshellarg($_POST['text']);

        // Construct the command to execute the Python script
        $command = "python3 process.py " . $number . " " . $text;

        // Execute the command and capture the output
        $output = shell_exec($command);

        // Display the results
        echo "<h2>Results:</h2>";
        echo "<pre>" . htmlspecialchars($output) . "</pre>"; // Use htmlspecialchars for security
    }

    // Get and display the public IP address (always displayed)
    $publicIP = trim(shell_exec('curl -4 ifconfig.io'));
    if (!empty($publicIP)) {
        echo "<p><strong>Public IP Address:</strong> " . htmlspecialchars($publicIP) . "</p>";
    } else {
        echo "<p><strong>Could not retrieve public IP address.</strong></p>";
    }
    ?>
</body>
</html>