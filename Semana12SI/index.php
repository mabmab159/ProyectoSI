<?php

class Paciente_model
{
    private $param = array();

    private function evaluarprolog($pares)
    {
        if (!file_exists("seic.pl"))
            die("No se puede localizar el archivo seic.pl, el directorio actual es: " . __DIR__);
        $X = '[';
        $i = 1;
        foreach ($pares as $par) {
            if (strlen($par) > 3) {
                list($idsintoma, $r) = explode(";", $par);
                if ($r == 's') {
                    $X .= 's' . $i . ',';
                }
            }
            $i++;
        }
        if (substr($X, -1, 1) == ',')
            $X = substr($X, 0, strlen($X) - 1);
        $X .= ']';
        /*$X = '[s1,s4,s10,s11]';*/

        $output = `swipl -s seic.pl -g "test($X)." -t halt.`;
        return $output;
    }

    public function realizarDiagnostico()
    {
        $pares = explode("#", $this->param['param_lista']);
        $resultado = $this->evaluarprolog($pares);

        // Interceptar respuesta con la BD
        $con = mysqli_connect("localhost", "root", "");
        mysqli_select_db($con, "semana12si");
        $nombre = $_POST["name"];
        $apellido = $_POST["apellido"];
        $query = mysqli_query($con, "insert into usuarios (nombre, apellido,diagnostico ) values ('$nombre','$apellido','$resultado')");
        return $resultado;
    }

    public function __construct($param)
    {
        $this->param = $param;
    }
}


$sintomas = [
    [
        "id" => "1",
        "nombre" => "Dolor de pecho",
    ],
    [
        "id" => "2",
        "nombre" => "Molestia de pecho",
    ],
    [
        "id" => "3",
        "nombre" => "Falta de aire",
    ],
    [
        "id" => "4",
        "nombre" => "Dolor general",
    ],
    [
        "id" => "5",
        "nombre" => "Entumecimiento",
    ],
    [
        "id" => "6",
        "nombre" => "Debilidad",
    ],
    [
        "id" => "7",
        "nombre" => "Sensacion de frio",
    ],
    [
        "id" => "8",
        "nombre" => "Dolor de garganta",
    ],
    [
        "id" => "9",
        "nombre" => "Opresion de pecho",
    ],
    [
        "id" => "10",
        "nombre" => "Latidos irregulares",
    ],
    [
        "id" => "11",
        "nombre" => "Aturdimiento",
    ],
    [
        "id" => "12",
        "nombre" => "Mareos",
    ],
    [
        "id" => "13",
        "nombre" => "Desmayos",
    ],
    [
        "id" => "14",
        "nombre" => "Hinchazon en la pierna",
    ],
    [
        "id" => "15",
        "nombre" => "Hinchazon en el abdomen",
    ],
    [
        "id" => "16",
        "nombre" => "Cansancio",
    ],
    [
        "id" => "17",
        "nombre" => "Fiebre",
    ],
    [
        "id" => "18",
        "nombre" => "Tos seca",
    ],
    [
        "id" => "19",
        "nombre" => "Erupciones cuteanas",
    ],
    [
        "id" => "20",
        "nombre" => "Falta de apetito",
    ],
];

$enfermedades = [
    "E1" => [
        "nombre" => "Ateroesclerosis",
        "img" => "https://www.nhlbi.nih.gov/sites/default/files/inline-images/Plaque-buildup-spanish.jpg",
    ],
    "E2" => [
        "nombre" => "Arritmias",
        "img" => "https://www.mayoclinic.org/-/media/kcms/gbs/patient-consumer/images/2013/08/26/10/42/typical-heartbeat_1709751_3881158-001-1-72ppi-8col.jpg",
    ],
    "E3" => [
        "nombre" => "miocardiopatia",
        "img" => "https://www.ecured.cu/images/thumb/b/bf/Cardiomiop_hipert_2.jpg/260px-Cardiomiop_hipert_2.jpg",
    ],
    "E4" => [
        "nombre" => "Endocarditis",
        "img" => "https://medlineplus.gov/spanish/ency/images/ency/fullsize/18132.jpg",
    ],
    "E5" => [
        "nombre" => "Valvulopatia",
        "img" => "https://www.institutocardiotecnologico.com/images/stories/blogicta_editoresmedicos/porras/valvulopatias-generalidades25.11.2013/valvulas-cardiacas.jpg",
    ],
    "E6" => [
        "nombre" => "Estenosis",
        "img" => "https://kidshealth.org/content/dam/patientinstructions/es/images/aorticSten_415x259_esIL.png",
    ],
    "E7" => [
        "nombre" => "Amiloidosis",
        "img" => "https://multimedia.elsevier.es/PublicationsMultimediaV1/item/multimedia/13137607:25v62n06-13137607fig02.jpg?idApp=UINPBA000025",
    ],
    "E8" => [
        "nombre" => "Infarto agudo de miocardio",
        "img" => "https://www.intramed.net/UserFiles/vinetas/94591.jpg",
    ],
];

?>
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>Hello, world!</title>
</head>

<body>
<div class="container mt-5">
    <div class="row">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">Formulario</div>
                <div class="card-body">
                    <form action='.' method='post'>
                        <div class="form-group mb-3">
                            <label for='param_nombre' class="form-label">Ingrese nombres:</label>
                            <input type='text' class="form-control" id='param_nombre' name='name' value='' required>
                        </div>
                        <div class="form-group mb-3">
                            <label for='param_apellido' class="form-label">Ingrese apellidos:</label>
                            <input type='text' class="form-control" id='param_apellido' name='apellido' value=''
                                   required>
                        </div>
                        <div class="form-group">
                            <div class="row px-3">
                                <?php foreach ($sintomas as $key => $sintoma) { ?>
                                    <div class="form-check col-md-6 mb-3">
                                        <input type='checkbox' id='param_enfermedad_<?= $sintoma["id"] ?>'
                                               name='param_lista<?= $sintoma["id"] ?>' class="form-check-input">
                                        <label for='param_enfermedad_<?= $sintoma["id"] ?>'
                                               class="form-check-label"><?= $sintoma["nombre"] ?></label>
                                    </div>
                                <?php } ?>
                            </div>
                        </div>
                        <input type='submit' value='Registrar' class='btn btn-success'>
                    </form>
                </div>
            </div>
        </div>
        <?php if ($_POST) {

            $params = [];

            $paramas = [
                isset($_POST["param_lista1"]) ? $_POST["param_lista1"] : "0",
                isset($_POST["param_lista2"]) ? $_POST["param_lista2"] : "0",
                isset($_POST["param_lista3"]) ? $_POST["param_lista3"] : "0",
                isset($_POST["param_lista4"]) ? $_POST["param_lista4"] : "0",
                isset($_POST["param_lista5"]) ? $_POST["param_lista5"] : "0",
                isset($_POST["param_lista6"]) ? $_POST["param_lista6"] : "0",
                isset($_POST["param_lista7"]) ? $_POST["param_lista7"] : "0",
                isset($_POST["param_lista8"]) ? $_POST["param_lista8"] : "0",
                isset($_POST["param_lista9"]) ? $_POST["param_lista9"] : "0",
                isset($_POST["param_lista10"]) ? $_POST["param_lista10"] : "0",
                isset($_POST["param_lista11"]) ? $_POST["param_lista11"] : "0",
                isset($_POST["param_lista12"]) ? $_POST["param_lista12"] : "0",
                isset($_POST["param_lista13"]) ? $_POST["param_lista13"] : "0",
                isset($_POST["param_lista14"]) ? $_POST["param_lista14"] : "0",
                isset($_POST["param_lista15"]) ? $_POST["param_lista15"] : "0",
                isset($_POST["param_lista16"]) ? $_POST["param_lista16"] : "0",
                isset($_POST["param_lista17"]) ? $_POST["param_lista17"] : "0",
                isset($_POST["param_lista18"]) ? $_POST["param_lista18"] : "0",
                isset($_POST["param_lista19"]) ? $_POST["param_lista19"] : "0",
                isset($_POST["param_lista20"]) ? $_POST["param_lista20"] : "0",
            ];

            foreach ($paramas as $key => $value) {
                $params[] = "$value;s";
            }

            $param["param_lista"] = implode("#", $params);

            $paciente_model = new Paciente_model($param);
            $resultado = $paciente_model->realizarDiagnostico();

            ?>
            <div class="col-md-6">
                <div class="card" style="width: 18rem;">
                    <?php if ($resultado) { ?>
                        <img src="<?= $enfermedades[$resultado]["img"] ?>" class="card-img-top" alt="img_enfermedad">
                        <div class="card-body">
                            <h5 class="card-title"><?= $_POST["name"] ?></h5>
                            <h6 class="card-subtitle mb-2 text-muted"><?= $_POST["apellido"] ?></h6>
                            <p class="card-text">Diagnostico completo.</p>
                            <p class="card-text">Resultado: <?= $enfermedades[$resultado]["nombre"] ?></p>
                        </div>
                    <?php } else { ?>
                        <div class="card-body">
                            <h5 class="card-title"><?= $_POST["name"] ?></h5>
                            <h6 class="card-subtitle mb-2 text-muted"><?= $_POST["apellido"] ?></h6>
                            <p class="card-text">No se pudo diagnosticar.</p>
                            <p class="card-text">Intente nuevamente.</p>
                        </div>
                    <?php } ?>
                </div>
            </div>
        <?php } ?>
    </div>
    <div style="margin-top: 25px">
        <h2 style="margin: 25px">Resumen de diagnosticos</h2>
        <div class="col-md-6">
            <table class="table">
                <thead>
                <tr>
                    <th>Id</th>
                    <th>Nombres</th>
                    <th>Apellidos</th>
                    <th>Diagnostico</th>
                </tr>
                </thead>
                <tbody>
                <?php
                $con = mysqli_connect("localhost", "root", "");
                mysqli_select_db($con, "semana12si");
                $historico = mysqli_fetch_all(mysqli_query($con, "select * from usuarios"));
                for ($i = 0; $i < count($historico); $i++) {
                    echo "<tr>";
                    for ($j = 0; $j < 3; $j++) {
                        echo "<td>{$historico[$i][$j]}</td>";
                    }
                    echo "<td>{$enfermedades[$historico[$i][3]]['nombre']}</td>";
                    echo "</tr>";
                }
                ?>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div>

</div>

<!-- Optional JavaScript; choose one of the two! -->

<!-- Option 1: Bootstrap Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
        crossorigin="anonymous"></script>

<!-- Option 2: Separate Popper and Bootstrap JS -->
<!--
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
-->
</body>