using System.Collections;
using UnityEngine.Networking;
using UnityEngine.UI;
using UnityEngine;
using Newtonsoft.Json;
using System.Text;
using System.IO;

struct Row {
    public string NAME;
    public int AGE;
    public string GENDER;
    public string COUNTRY;
    public string JOB;
    public string EMAIL;
    public string PHONE;
}
public class HandleButtons : MonoBehaviour{
    public InputField setName;
    public InputField setAge;
    public InputField setGender;
    public InputField setCountry;
    public InputField setJob;
    public InputField setEmail;
    public InputField setPhone;
    private byte[] data;
    private string json;

    public void AddToDB() {
        StartCoroutine(Upload());
    }

    IEnumerator Upload() {
        Row veri = new Row();
        veri.NAME = setName.text.Trim();
        veri.AGE = int.Parse(setAge.text.Trim());
        veri.GENDER = setGender.text.Trim();
        veri.COUNTRY = setCountry.text.Trim();
        veri.JOB = setJob.text.Trim();
        veri.EMAIL = setEmail.text.Trim();
        veri.PHONE = setPhone.text.Trim();
        json = JsonConvert.SerializeObject(veri);
        data = Encoding.UTF8.GetBytes(json);

		// Put() will contain the address of server where getrow.php and register.db files will be stored.
		// Here, "localhost" is used as those files are placed in "htdocs" folder of the XAMPP web server:
        UnityWebRequest www = UnityWebRequest.Put("http://localhost/getrow.php", data);
        yield return www.SendWebRequest();

        if (www.isNetworkError || www.isHttpError)
            Debug.Log(www.error);
        else
            Debug.Log("Upload Successful!");

    }
}
