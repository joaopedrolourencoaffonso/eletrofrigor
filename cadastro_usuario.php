<?php
$user = 'joao';
$pass = 'senha';
$db = 'eletrofrigor';

$con = new mysqli('localhost', $user, $pass, $db);

if (mysqli_connect_errno()) {
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$nome = $_POST["nome"];
$idade = $_POST["idade"];
$cpf = $_POST["cpf"];
$senha1 = $_POST["senha1"];
$senha2 = $_POST["senha2"];

$sql = "select * from usuarios where nome = '$nome' or cpf = '$cpf';";
$result = $con-> query($sql);

if ($result-> num_rows > 0) {
	print("Desculpe, nome de usuário ou número de cpf já cadastrado!");
	exit;
}


$sql = "insert into usuarios (nome, idade, cpf, senha) values ('$nome', $idade, $cpf, '$senha1')";

if ($senha1 == $senha2) {
	if ($con->query($sql) === TRUE) {
	    echo "Usuario criado com sucesso!";
	} else {
	    echo "Error: " . $sql . "<br>" . $con->error;
	}
} else {
	print("Você digitou a senha errado, por favor, tente de novo.");
}
?>