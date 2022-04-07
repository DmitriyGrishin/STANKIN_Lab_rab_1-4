<?php

require_once "connect.php";

header('Content-Encoding: UTF-8');
header('Content-type: text/csv; charset=UTF-8');
header("Content-disposition: attachment; filename=export.csv");
header("Pragma: public");
header("Expires: 0");
echo "\xEF\xBB\xBF";

$sql = "SELECT * FROM form";
$result = $conn->query($sql);

$fp = fopen('php://output', 'w');

while($row = $result->fetch_assoc()) { 
    $row = fputcsv($fp, $row, ";"); 
}

$conn->close(); 

?>
