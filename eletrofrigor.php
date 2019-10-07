<?php
$user = 'joao';
$pass = 'senha';
$db = 'eletrofrigor';

$db = mysqli_connect('localhost', $user, $pass, $db);

if (mysqli_connect_errno()) {
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$nome = $_POST["login"];
$senha = $_POST["senha"];

print("<!DOCTYPE html>
<html>
<p>Olá $nome! <br> Deseja cadastrar alguém hoje? </p>
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
	.nota {
	  background-color: lightgrey;
	  margin: 20px;
	}
   </style>
</head>
<body>

<div class='center'>
<p>Empresas das quais você faz parte</p>
</div>

   <table>
       <tr> 
	<th>ID</th>
	<th>Nome</th>
	<th>CNPJ</th>
	</tr>
</body>");

$sql = "select * from usuarios;";
$result = $db-> query($sql);

if ($result-> num_rows > 0) {
	while ($row = $result-> fetch_assoc()) {
		if ($row["nome"] == $nome and $row["senha"] == $senha) {
			$temp = $row["id_user"];
			break;
		}
	}
	$sql = "select * from relacionamento as tab1 inner join empresas as tab2 on tab1.id_empresa = tab2.id_empresa where tab1.id_user = $temp";
	$result2 = $db-> query($sql);
	while ($row = $result2-> fetch_assoc()) {
		echo "<tr><td>".$row["id_empresa"]."</td><td>".$row["nome"]."</td><td>".$row["cnpj"]."</td></tr>";
	}
}

echo "</table>";

print("

<div class='center'>
<p>Cadastre um novo usuário!</p>
</div>

<form method='POST' action='cadastro_usuario.php'>
		Nome: <input type='text' placeholder='Joao Pedro' name='nome'/><br>
		Idade: <input type='text' placeholder='21' name='idade'/><br>
		CPF: <input type='text' placeholder='1234567890' name='cpf'/><br>
		senha: <input type='text' placeholder='senha' name='senha1'/><br>
		repita a senha por favor: <input type='text' placeholder='senha' name='senha2'/><br>
		<input type='submit' value='Cadastrar'/>
</form>

<div class='nota'>
<p>CUIDADO! Não use acentos ou (ç) para o nome de usuário ou empresa</p>
</div>

<div class='center'>
<p>Cadastre uma nova empresa!</p>
</div>
<form method='POST' action='cadastro_empresa.php'>
		Nome: <input type='text' placeholder='Eletrofrigor' name='nome'/><br>
		CNPJ: <input type='text' placeholder='12345678901' name='cnpj'/><br>
		<input type='submit' value='Cadastrar'/>
</form>

<div class='center'>
<p>Associe usuários a suas empresas!</p>
</div>
<form method='POST' action='associador.php'>
		Nome do usuario: <input type='text' placeholder='Joao' name='user'/><br>
		Nome da empresa: <input type='text' placeholder='Eletrofrigor' name='empresa'/><br>
		<input type='submit' value='Associar'/>
</form>

<div class='center'>
<p>Deletar registros</p>
</div>
<form method='POST' action='deleter.php'>
	Nome: <input type='text' placeholder='nome' name='nome'/><br>
	<fieldset><legend>Você quer deletar um(a):</legend>
		<input type='radio' name='oper' value='1' id='empresa'/>
		<label  for='empresa'>Empresa</label>
		<input type='radio' name='oper' value='2' id='user'/>
		<label  for='user'>Usuário</label>
		<input type='radio' name='oper' value='3' id='user'/>
		<label  for='relacao'>Relação</label>
	</fieldset>
	<input type='submit' value='Deletar'/>
</form>

<div class='nota'>
<p>Para excluir um relacionamento específico, basta digitar o nome do usuário seguido do nome da empresa, ambos separados por '|', ex: Maria|Coca-cola)</p>
</div>

<div class='center'>
<p>Veja as associações existentes</p>
</div>
<form method='POST' action='associacoes.php'>
	Nome: <input type='text' placeholder='nome' name='nome'/><br>
	<fieldset><legend>Você quer ver as associações de um(a):</legend>
		<input type='radio' name='oper' value='1' id='empresa'/>
		<label  for='empresa'>Empresa</label>
		<input type='radio' name='oper' value='2' id='user'/>
		<label  for='user'>Usuário</label>
	</fieldset>
	<input type='submit' value='Visualizar'/>
</form>");

print("</html>");

?>