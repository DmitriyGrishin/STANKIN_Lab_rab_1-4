<?php

$servername = "lab";
$username = "root";
$password = "";
$db = "lab_rab";

$conn = new mysqli($servername, $username, $password, $db);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
?>
