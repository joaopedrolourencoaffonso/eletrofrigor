<?php
$user = 'joao';
$pass = 'senha';
$db = 'eletrofrigor';

$con = new mysqli('localhost', $user, $pass, $db);

if (mysqli_connect_errno()) {
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$user = $_POST["user"];
$empresa = $_POST["empresa"];

###################################secao para evitar entradas erradas
$sql = "select * from usuarios as tab1 inner join relacionamento as tab2 on tab1.id_user = tab2.id_user inner join empresas as tab3 on tab3.id_empresa = tab2.id_empresa where tab3.nome = '$empresa' and tab1.nome = '$user';";
$result = $con-> query($sql);

if ($result-> num_rows > 0) {
	print("Desculpe, $user já está associado a $empresa!");
	exit;
}

$sql = "select * from empresas where nome = '$empresa';";
$result = $con-> query($sql);

if ($result-> num_rows == 0) {
	print("Desculpe, a empresa '$empresa', não existe!");
	exit;
}

$sql = "select * from usuarios where nome = '$user';";
$result = $con-> query($sql);

if ($result-> num_rows == 0) {
	print("Desculpe, o usuário '$user', não existe!");
	exit;
}

exit;
###################################

$sql = "insert into relacionamento (id_empresa, id_user) select tab2.id_empresa, tab1.id_user from usuarios as tab1 inner join empresas as tab2 on tab2.nome != tab1.nome where tab2.nome = '$empresa' and tab1.nome = '$user';";
if ($con->query($sql) === TRUE) {
    echo "Relação feita com sucesso!";
} else {
    echo "Error: " . $sql . "<br>" . $con->error;
}
?>