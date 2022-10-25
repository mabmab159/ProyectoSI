<?php require_once "bd.php";
$query = mysqli_query($con, "select * from sintomas");
$resultados = mysqli_fetch_all($query);
return $resultados;