using System;
using System.IO;
using System.Net;
using System.Windows.Forms;

namespace ScenarioMaker
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //HttpWebRequest httpWebRequest = (HttpWebRequest)WebRequest.Create("http://host/files/" + Environment.UserName.ToString().Replace("\n", "").Replace("\r", "") + "/");
            HttpWebRequest httpWebRequest = (HttpWebRequest)WebRequest.Create("http://host/scenarios/");
            httpWebRequest.KeepAlive = false;
            HttpWebResponse response = (HttpWebResponse)httpWebRequest.GetResponse();
            Stream stream = response.GetResponseStream();
            StreamReader streamReader = new StreamReader(stream);
            var responseResult = streamReader.ReadToEnd();
            for (int i = 0; i < responseResult.Split('\"').Length; i++)
            {
                if (responseResult.Split('\"')[i].Contains("href="))
                {
                    listBox1.Items.Add(responseResult.Split('\"')[i + 1]);
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string downloadFile = listBox1.SelectedItem.ToString();
            //HttpWebRequest httpWebRequest = (HttpWebRequest)WebRequest.Create("http://host/files/" + Environment.UserName.ToString().Replace("\n", "").Replace("\r", "") + "/" + downloadFile);
            HttpWebRequest httpWebRequest = (HttpWebRequest)WebRequest.Create("http://host/scenarios/" + downloadFile);
            HttpWebResponse response = (HttpWebResponse)httpWebRequest.GetResponse();
            Stream stream = response.GetResponseStream();
            StreamReader streamReader = new StreamReader(stream);
            var responseResult = streamReader.ReadToEnd();
            if (File.Exists(Directory.GetCurrentDirectory() + "/scenarios/" + downloadFile))
            {
                downloadFile = downloadFile + ".0";
            }
            File.Create(Directory.GetCurrentDirectory() + "/scenarios/" + downloadFile).Close();
            File.WriteAllText(Directory.GetCurrentDirectory() + "/scenarios/" + downloadFile, responseResult);
            MessageBox.Show("File successfully downloaded");

        }
    }
}
