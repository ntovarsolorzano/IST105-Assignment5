<!DOCTYPE html>
<html>
<head>
    <title>Interactive Treasure Hunt</title>
</head>
<body>

<h1>Solve the Puzzle!</h1>

<form action="process.py" method="POST">
    <label for="number">Enter a Number (e.g., Birth Year):</label><br>
    <input type="number" id="number" name="number" required><br><br>

    <label for="text">Enter a Text Message (e.g., Name):</label><br>
    <input type="text" id="text" name="text" required><br><br>

    <input type="submit" value="Solve the Puzzle">
</form>

<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Check if the Python script was successful
        if (isset($_GET["number_result"]) && isset($_GET["text_binary"]) && isset($_GET["treasure_result"])) {
            echo "<h2>Results:</h2>";
            echo "<p><b>Number Puzzle:</b> " . $_GET["number_result"] . "</p>";
            echo "<p><b>Text to Binary:</b> " . $_GET["text_binary"] . "</p>";
            echo "<p><b>Vowel Count:</b> " . $_GET["vowel_count"] . "</p>";
            echo "<p><b>Treasure Hunt:</b> " . $_GET["treasure_result"] . "</p>";
        } else {
            echo "<p>Error processing data. Please try again.</p>";
        }
    }
?>

</body>
</html>