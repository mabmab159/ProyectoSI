<?php require_once "bd.php";
$query = mysqli_query($con, "select * from diagnosticos");
return mysqli_fetch_all($query);
