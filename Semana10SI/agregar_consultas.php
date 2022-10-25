<?php
require_once "bd.php";
$arreglo = "";
for ($i = 1; $i <= 5; $i++) {
    if (isset($_POST[$i])) {
        $arreglo = $arreglo . "s" . $i . ",";
    }
}
$arreglo = "[" . substr($arreglo, 0, strlen($arreglo) - 1) . "]";
$output = `swipl -s evaluacion.pl -g "listar_sintomas($arreglo)." -t halt.`;
$nombre = $_POST["nombre"];
$apellido = $_POST["apellido"];
$diagnostico = strlen($output) == 0 ? "Sin diagnostico" : $output;
$query = mysqli_query($con, "insert into diagnosticos (nombre,apellido,diagnostico) values ('$nombre', '$apellido', '$diagnostico')");
header("Location: " . "./index.php");