<?php
$user = 'joao';
$pass = 'senha';
$db = 'eletrofrigor';

$con = new mysqli('localhost', $user, $pass, $db);

if (mysqli_connect_errno()) {
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$nome = $_POST["nome"];
$oper = $_POST["oper"];

if ($oper == 2) {
	print("<!DOCTYPE html>
<html>
<head> 
   <title>Bem vindo</title>
   <style type='text/css'>
	table {
		border-collapse: collapse;
		width: 100%;
		color: #d96459;
		font-family: monospace; 
		font-size: 25px;
		text-align: left;
	}
	th {
		background-color: #588c7e;
		color: white;
	}
	.center {
	  text-align: center;
	  margin: auto;
	  width: 60%;
	  padding: 10px;
	  font-size: 30px
	}
   </style>
</head>
<body>

<div class='center'>
<p>Empresas das quais $nome faz parte</p>
</div>

   <table>
       <tr> 
	<th>ID</th>
	<th>Nome</th>
	<th>CNPJ</th>
	</tr>
</body>");

	$sql = "select * from usuarios;";
	$result = $con-> query($sql);

	if ($result-> num_rows > 0) {
		while ($row = $result-> fetch_assoc()) {
			if ($row["nome"] == $nome) {
				$temp = $row["id_user"];
				break;
			}
		}
		$sql = "select * from relacionamento as tab1 inner join empresas as tab2 on tab1.id_empresa = tab2.id_empresa where tab1.id_user = $temp";
		$result2 = $con-> query($sql);
		while ($row = $result2-> fetch_assoc()) {
			echo "<tr><td>".$row["id_empresa"]."</td><td>".$row["nome"]."</td><td>".$row["cnpj"]."</td></tr>";
		}
	}

	echo "</table>";

} else {
	print("<!DOCTYPE html>
<html>
<head> 
   <title>Bem vindo</title>
   <style type='text/css'>
	table {
		border-collapse: collapse;
		width: 100%;
		color: #d96459;
		font-family: monospace; 
		font-size: 25px;
		text-align: left;
	}
	th {
		background-color: #588c7e;
		color: white;
	}
	.center {
	  text-align: center;
	  margin: auto;
	  width: 60%;
	  padding: 10px;
	  font-size: 30px
	}
   </style>
</head>
<body>

<div class='center'>
<p>Empresas das quais $nome faz parte</p>
</div>

   <table>
       <tr> 
	<th>ID</th>
	<th>Nome</th>
	<th>Idade</th>
	<th>CPF</th>
	</tr>
</body>");

	$sql = "select * from empresas;";
	$result = $con-> query($sql);

	if ($result-> num_rows > 0) {
		while ($row = $result-> fetch_assoc()) {
			if ($row["nome"] == $nome) {
				$temp = $row["id_empresa"];
				break;
			}
		}
		$sql = "select * from relacionamento as tab1 inner join usuarios as tab2 on tab1.id_user = tab2.id_user where tab1.id_empresa = $temp";
		$result2 = $con-> query($sql);
		while ($row = $result2-> fetch_assoc()) {
			echo "<tr><td>".$row["id_user"]."</td><td>".$row["nome"]."</td><td>".$row["idade"]."</td><td>".$row["cpf"]."</td></tr>";
		}
	}

	echo "</table>";
}

?>