<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Registrar sintomas</title>
    <link href="style.css" rel="stylesheet" type="text/css">
</head>
<body>
<?php
$resultado = require_once("obtener_lista_sintomas.php");
$consultas = require_once("buscar_consultas.php");
?>
<h4>Registrar usuario y sintomas</h4>
<form action="agregar_consultas.php" method="post">
    <label style="display: block">Ingrese nombres:
        <input type="text" name="nombre" required>
    </label>
    <label style="display: block">Ingrese apellidos:
        <input type="text" name="apellido" required>
    </label>
    <ul>
        <?php
        for ($i = 0; $i < count($resultado); $i++) {
            $j = $i + 1;
            echo "<li><input type='checkbox' value='1' name='$j'>{$resultado[$i][1]}</input></li>";
        }
        ?>
    </ul>
    <button type="submit">Registrar</button>
</form>
<h4>Listado de consultas</h4>
<table>
    <thead>
    <tr>
        <td>Id</td>
        <td>Nombre</td>
        <td>Apellido</td>
        <td>Diagnostico</td>
    </tr>
    </thead>
    <tbody>
    <?php
    for ($i = 0; $i < count($consultas); $i++) {
        echo "<tr>";
        for ($j = 0; $j < 4; $j++) {
            echo "<td>{$consultas[$i][$j]}</td>";
        }
        echo "</tr>";
    }
    ?>
    </tbody>
</table>
</body>

</html>