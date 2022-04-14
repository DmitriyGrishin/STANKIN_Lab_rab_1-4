<?php

require_once "connect.php";

$surname = $_POST['surname'];
$name = $_POST['name'];
$group = $_POST['grp'];

$query = "INSERT INTO `form` (`id`, `surname`, `name`, `grp`) VALUES (NULL, '$surname', '$name', '$grp')";
    if ($conn->query($query) === TRUE)
    {
    $conn->close();
    }

header('Location: ../');

?>
