<?php

require_once "connect.php";
require_once "phpexcel/classes/PHPExcel.php";

 $objPHPExcel = new PHPExcel();

 $query = "SELECT * FROM form";
 $result = mysqli_query($conn, $query);
 $rowCount = 1;

while($row = mysqli_fetch_array($result)){
$objPHPExcel->getActiveSheet()->SetCellValue('A'.$rowCount, $row['id']);
$objPHPExcel->getActiveSheet()->SetCellValue('B'.$rowCount, $row['surname']);
$objPHPExcel->getActiveSheet()->SetCellValue('C'.$rowCount, $row['name']);
$objPHPExcel->getActiveSheet()->SetCellValue('D'.$rowCount, $row['grp']);
$rowCount++;
}

 header('Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet');
 header('Content-Disposition: attachment;filename="exportfile.xlsx"');
 header('Cache-Control: max-age=0');

 $objWriter = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
 $objWriter->save('php://output');

?>
