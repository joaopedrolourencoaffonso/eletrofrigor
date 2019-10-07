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

#print("$nome e $oper");

if ($oper == 2) {
	$sql = "select * from usuarios;";
} elseif ($oper == 1) {
	$sql = "select * from empresas;";
} else {
	$array = explode("|",$nome);
	$sql = "select tab2.id_empresa, tab1.id_user from usuarios as tab1 inner join empresas as tab2 on tab2.nome != tab1.nome where tab2.nome = '$array[1]' and tab1.nome = '$array[0]';";
}

$result = $con-> query($sql);

if ($result-> num_rows > 0) {
	while ($row = $result-> fetch_assoc()) {
		if ($oper == 3) {
			$id_empresa = $row["id_empresa"];
			$id_user = $row["id_user"];
			break;
		} else {
			if ($row["nome"] == $nome and $oper == 2) {
				$id = $row["id_user"];
				break;
			} elseif ($row["nome"] == $nome and $oper == 1) {
				$id = $row["id_empresa"];
				break;
			} 
		}
	}
}

if ($oper == 2) {
	$sql = "delete from usuarios where id_user = $id;";
} elseif ($oper == 1) {
	$sql = "delete from empresas where id_empresa = $id;";
} else {
	$sql = "delete from relacionamento where id_empresa = $id_empresa and id_user = $id_user;";
}

if ($con->query($sql) === TRUE) {
    echo "Banco de dados alterado com sucesso!";
} else {
    echo "Error: " . $sql . "<br>" . $con->error;
}

if ($oper == 2) {
	$sql = "delete from relacionamento where id_user = $id;";
} elseif ($oper == 1) {
	$sql = "delete from relacionamento where id_empresa = $id;";
} else {
	$sql = "delete from relacionamento where id_empresa = $id_empresa and id_user = $id_user;";
}

if ($con->query($sql) === TRUE) {
    echo "Banco de dados alterado com sucesso!";
} else {
    echo "Error: " . $sql . "<br>" . $con->error;
}

?>