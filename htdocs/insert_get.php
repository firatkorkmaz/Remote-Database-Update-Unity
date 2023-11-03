<?php

$name = $_GET["name"];
$age = $_GET["age"];
$gender = $_GET["gender"];
$country = $_GET["country"];
$job = $_GET["job"];
$email = $_GET["email"];
$phone = $_GET["phone"];

if(!ctype_digit($age)){
	echo "Please enter the Age as an integer!";
	return;
}


$dbFile = "register.db";
$db = new PDO("sqlite:$dbFile");

$db->exec("INSERT INTO Contact (EMAIL, PHONE) VALUES ('$email', '$phone');") or die(print_r($db->errorInfo(), true));
$coid = $db->lastInsertId();

$db->exec("INSERT INTO Info (COUNTRY, JOB, CO_ID) VALUES ('$country', '$job', '$coid');") or die(print_r($db->errorInfo(), true));
$infoid = $db->lastInsertId();

$db->exec("INSERT INTO Customer (NAME, AGE, GENDER, INFO_ID) VALUES ('$name', '$age', '$gender', '$infoid');") or die(print_r($db->errorInfo(), true));
$cuid = $db->lastInsertId();


// Printing the New Entry in the Database
echo "New Entry is Recorded in the Database: $dbFile</br>";
echo $cuid . ") ";
echo "Name: " . $name . " || ";
echo "Age: " . $age . " || ";
echo "Gender: " . $gender . " || ";
echo "Country: " . $country . " || ";
echo "Job: " . $job . " || ";
echo "E-Mail: " . $email . " || ";
echo "Phone: " . $phone;
echo "</br></br>";


// Printing the List of All the Entries in the Database
$sql = "SELECT * FROM Customer INNER JOIN Info ON Customer.INFO_ID = Info.INFO_ID INNER JOIN Contact ON Info.CO_ID = Contact.CO_ID;";
$result = $db->query($sql);

echo "The List of All the Entries in the Database: $dbFile</br>";
foreach($result as $row){
	echo $row['CU_ID'] . ") ";
	echo "Name: " . $row['NAME'] . " || ";
	echo "Age: " . $row['AGE'] . " || ";
	echo "Gender: " . $row['GENDER'] . " || ";
	//echo $row['INFO_ID'] . " || ";
	echo "Country: " . $row['COUNTRY'] . " || ";
	echo "Job: " . $row['JOB'] . " || ";
	//echo $row['CO_ID'] . " || ";
	echo "E-Mail: " . $row['EMAIL'] . " || ";
	echo "Phone: " . $row['PHONE'];
	echo "<br>";
}

?>