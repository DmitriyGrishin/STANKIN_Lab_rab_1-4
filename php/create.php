<?php

require_once "connect.php";

$surname = $_POST['surname'];
$name = $_POST['name'];
$group = $_POST['group'];

$query = "INSERT INTO `form` (`id`, `surname`, `name`, `grp`) VALUES (NULL, '$surname', '$name', '$group')";
    if ($conn->query($query) === TRUE)
    {
    $conn->close();
    }

header('Location: ../');

?>