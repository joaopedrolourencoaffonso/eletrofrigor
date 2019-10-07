<?php
$user = 'joao';
$pass = 'senha';
$db = 'eletrofrigor';

$con = new mysqli('localhost', $user, $pass, $db);

if (mysqli_connect_errno()) {
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$nome = $_POST["nome"];
$cnpj = $_POST["cnpj"];

$sql = "select * from empresas where nome = '$nome' or cnpj = '$cnpj';";
$result = $con-> query($sql);

if ($result-> num_rows > 0) {
	print("Desculpe, nome de empresa ou número de cnpj já cadastrado!");
	exit;
}

$sql = "insert into empresas (nome, cnpj) values ('$nome', $cnpj)";

if ($con->query($sql) === TRUE) {
    echo "Empresa cadastrada com sucesso!";
} else {
    echo "Error: " . $sql . "<br>" . $con->error;
}
?>