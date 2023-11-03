<?php
//header('Content-Type: text/plain');

$dbFile = "register.db";
$db = new PDO("sqlite:$dbFile");

//$sql = "SELECT CU_ID, NAME, AGE, GENDER, COUNTRY, JOB, EMAIL, PHONE FROM Customer INNER JOIN Info ON Customer.INFO_ID = Info.INFO_ID INNER JOIN Contact ON Info.CO_ID = Contact.CO_ID;";

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