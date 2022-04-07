using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading;
using System.Windows.Forms;

namespace ScenarioMaker
{
    public partial class nexusTake : Form
    {
        List<string> reposNames = new List<string>();
        public Thread thread0;
        Form1 form1;
        public nexusTake(Form1 frm1)
        {
            InitializeComponent();
            this.form1 = frm1;
        }

        public string postRequestToGetData(string json)
        {
            var body = Encoding.UTF8.GetBytes(json);
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create("https://repoDomain/service/extdirect");
            request.Method = "POST";
            request.ContentType = "application/json";
            request.ContentLength = body.Length;
            Stream stream = request.GetRequestStream();
            stream.Write(body, 0, body.Length);
            stream.Close();
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            var responseString = new StreamReader(response.GetResponseStream()).ReadToEnd();
            return responseString;
        }

        private void nexusTake_Load(object sender, EventArgs e)
        {
            textBox4.ReadOnly = true;
            sameRequestsLoadPage();
            var repoPostData = "{ 'action':'coreui_Repository','method':'readReferences','data':[{ 'page':1,'start':0,'limit':25}],'type':'rpc','tid':3}";
            string responseString = postRequestToGetData(repoPostData);
            for (int i = 0; i < responseString.Split(new[] { "repositoryName" }, StringSplitOptions.None).Count(); i++)
            {
                var repo = responseString.Split(new[] { "repositoryName" }, StringSplitOptions.None)[i];
                var addedItem = repo.Split(new[] { "\":\"" }, StringSplitOptions.None)[1].Split(new[] { "\",\"online\":" }, StringSplitOptions.None)[0];
                if (!addedItem.Contains("\""))
                {
                    reposNames.Add(addedItem);
                    //checkedListBox1.Items.Add(addedItem);
                    treeView1.Nodes.Add(addedItem);
                }
            }

        }

        public async void sameRequestsLoadPage()
        {
            List<Array> headers = new List<Array>();
            headers.Add(new[] { "authority", "repoDomain" });
            headers.Add(new[] { "accept", "*/*" });
            headers.Add(new[] { "accept-language", "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7" });
            headers.Add(new[] { "cookie", "NX-ANTI-CSRF-TOKEN=0.09213723604687796" });
            headers.Add(new[] { "dnt", "1" });
            headers.Add(new[] { "nx-anti-csrf-token", "0.09213723604687796" });
            headers.Add(new[] { "origin", "https://repoDomain" });
            headers.Add(new[] { "referer", "https://repoDomain/" });
            headers.Add(new[] { "sec-ch-ua", "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"" });
            headers.Add(new[] { "sec-ch-ua-mobile", "?0" });
            headers.Add(new[] { "sec-ch-ua-platform", "\"Windows\"" });
            headers.Add(new[] { "sec-fetch-dest", "empty" });
            headers.Add(new[] { "sec-fetch-mode", "cors" });
            headers.Add(new[] { "sec-fetch-site", "same-origin" });
            headers.Add(new[] { "sec-gpc", "1" });
            headers.Add(new[] { "user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36" });
            headers.Add(new[] { "x-nexus-ui", "true" });
            headers.Add(new[] { "x-requested-with", "XMLHttpRequest" });
            var handler = new HttpClientHandler();
            using (var httpClient = new HttpClient(handler))
            {
                using (var request = new HttpRequestMessage(new HttpMethod("POST"), "https://repoDomain/service/extdirect"))
                {
                    foreach (var header in headers)
                    {
                        request.Headers.TryAddWithoutValidation(header.GetValue(0).ToString(), header.GetValue(1).ToString());
                    }
                    request.Content = new StringContent("{\"action\":\"node_NodeAccess\",\"method\":\"nodes\",\"data\":null,\"type\":\"rpc\",\"tid\":1}");
                    request.Content.Headers.ContentType = MediaTypeHeaderValue.Parse("application/json");

                    var response = await httpClient.SendAsync(request);
                }
                label1.Invoke((MethodInvoker)(() => label1.Text = "1 request"));
                using (var request = new HttpRequestMessage(new HttpMethod("POST"), "https://repoDomain/service/extdirect"))
                {
                    foreach (var header in headers)
                    {
                        request.Headers.TryAddWithoutValidation(header.GetValue(0).ToString(), header.GetValue(1).ToString());
                    }
                    request.Content = new StringContent("{\"action\":\"rapture_Security\",\"method\":\"getPermissions\",\"data\":null,\"type\":\"rpc\",\"tid\":2}");
                    request.Content.Headers.ContentType = MediaTypeHeaderValue.Parse("application/json");

                    var response = await httpClient.SendAsync(request);
                    label1.Invoke((MethodInvoker)(() => label1.Text = "2 request"));
                }

            }
        }
        public void downloadingNeededModules()
        {
            //foreach (var item in checkedListBox1.CheckedItems)
            //{
            //    List<string> links = new List<string>();
            //    var json = "{'action':'coreui_Browse','method':'read','data':[{'repositoryName':'" + item.ToString() + "','node':'master'}],'type':'rpc','tid':6}";
            //    var body = Encoding.UTF8.GetBytes(json);
            //    HttpWebRequest request = (HttpWebRequest)WebRequest.Create("https://repoDomain/service/extdirect");
            //    request.Method = "POST";
            //    request.ContentType = "application/json";
            //    request.ContentLength = body.Length;
            //    Stream stream = request.GetRequestStream();
            //    stream.Write(body, 0, body.Length);
            //    stream.Close();
            //    HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            //    var responseString = new StreamReader(response.GetResponseStream()).ReadToEnd();
            //    label1.Invoke((MethodInvoker)(() => label1.Text = "Final request"));
            //    for (int i = 0; i < responseString.Split(new[] { "\"id\":" }, StringSplitOptions.None).Count(); i++)
            //    {
            //        try
            //        {
            //            var repo = responseString.Split(new[] { "\"id\":" }, StringSplitOptions.None)[i + 1];
            //            var addedItem = repo.Split(new[] { "\"" }, StringSplitOptions.None)[1].Split(new[] { "\", \"text\":" }, StringSplitOptions.None)[0];
            //            if (!addedItem.Contains("\""))
            //            {
            //                links.Add(addedItem);
            //            }
            //        }
            //        catch { }

            //    }
            //    string lastVersionOfmaster = "";
            //    double date = 0;
            //    foreach (string link in links)
            //    {
            //        try
            //        {
            //            if (date < double.Parse(link.Split('.')[link.Split('.').Count() - 5]))
            //            {
            //                date = double.Parse(link.Split('.')[link.Split('.').Count() - 5]);
            //                lastVersionOfmaster = link;
            //            }
            //        }
            //        catch { }
            //    }
            //    var urlLink = $"https://repoDomain/repository/{item}/{lastVersionOfmaster}";
            //    //waitForResponse(Form1.ssh.RunCommand("mkdir /root/modules/"));
            //    //var pochemuTiNeRabotaesh = lastVersionOfmaster.Replace("master/", "");
            //    //label1.Invoke((MethodInvoker)(() => label1.Text = "Wget start downloading"));
            //    //var output = waitForResponse(Form1.ssh.RunCommand($"wget -q -O /root/modules/{pochemuTiNeRabotaesh} {urlLink}"));
            //    //label1.Invoke((MethodInvoker)(() => label1.Text = "Ready"));
            //    //waitForResponse(Form1.ssh.RunCommand($"yum -y -v install /root/modules/{pochemuTiNeRabotaesh}"));

            //}
        }
        private void button1_Click(object sender, EventArgs e)
        {
            form1.adder(textBox2.Text);
        }

        public static List<string> listWithCheckedItems = new List<string>();

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            for (int i = 0; i < treeView1.Nodes.Count; i++)
            {
                if (!listWithCheckedItems.Contains(treeView1.Nodes[i].Text)) { listWithCheckedItems.Add(treeView1.Nodes[i].Text); }
            }
            treeView1.Nodes.Clear();
            foreach (var item in reposNames)
            {
                if (item.ToLower().Contains(textBox1.Text.ToLower()))
                {
                    if (listWithCheckedItems.Contains(item))
                    {
                        treeView1.Nodes.Add(item);
                    }
                    else { }
                }
            }
            if (textBox1.Text.Length == 0)
            {
                listWithCheckedItems.Clear();
            }

            //foreach (string item in checkedListBox1.CheckedItems)
            //{
            //    if (!listWithCheckedItems.Contains(item)) { listWithCheckedItems.Add(item); }
            //}
            //checkedListBox1.Items.Clear();
            //foreach (var item in reposNames)
            //{
            //    if (item.Contains(textBox1.Text))
            //    {
            //        if (listWithCheckedItems.Contains(item))
            //        {
            //            checkedListBox1.Items.Add(item, true);
            //        }
            //        else
            //        {
            //            checkedListBox1.Items.Add(item);
            //        }
            //    }
            //}
            //if (textBox1.Text.Length == 0)
            //{
            //    listWithCheckedItems.Clear();
            //}
        }

        private void checkedListBox1_MouseClick(object sender, MouseEventArgs e)
        {
            //checkedListBox1.SetItemChecked(checkedListBox1.SelectedIndex, true);
        }

        private void nexusTake_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (thread0 != null) try { thread0.Abort(); } catch { }
        }

        private void checkedListBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void responseFormatter(string responseString)
        {
            for (int i = 0; i < responseString.Split('\"').Count(); i++)
            {
                if (responseString.Split('\"')[i].Contains("id"))
                {
                    if (responseString.Split('\"')[i + 2] != "action")
                    {
                        treeView1.SelectedNode.Nodes.Add(responseString.Split('\"')[i + 2]);
                    }
                }
            }
        }
        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            treeView1.SelectedNode.Checked = true;
            string postData = "";
            if (treeView1.SelectedNode.FullPath.Split('\\').Length == 1)
            {
                postData = "{ 'action':'coreui_Browse','method':'read','data':[{ 'repositoryName':'" + treeView1.SelectedNode.Text + "','node':'/'}],'type':'rpc','tid':13}";
            }
            else if (treeView1.SelectedNode.FullPath.Split('\\').Length == 2)
            {
                postData = "{ 'action':'coreui_Browse','method':'read','data':[{ 'repositoryName':'" + treeView1.SelectedNode.Parent.Text + "','node':'" + treeView1.SelectedNode.Text + "'}],'type':'rpc','tid':14}";
            }
            else if (treeView1.SelectedNode.FullPath.Split('\\').Length > 2 && !treeView1.SelectedNode.Text.Contains(".rpm"))
            {
                string nodeForm = treeView1.SelectedNode.FullPath.Replace(treeView1.SelectedNode.Parent.FullPath, "");
                nodeForm = nodeForm.Replace("\\", "");
                postData = "{ 'action':'coreui_Browse','method':'read','data':[{ 'repositoryName':'" + treeView1.SelectedNode.Parent.Parent.Text + "','node':'" + nodeForm + "'}],'type':'rpc','tid':14}";
            }
            if (!treeView1.SelectedNode.Text.Contains(".rpm"))
            {
                string responseString = postRequestToGetData(postData);
                responseFormatter(responseString);
            }
            if (treeView1.SelectedNode.Text.Contains(".rpm"))
            {
                string filename = treeView1.SelectedNode.Text.Split('/')[treeView1.SelectedNode.Text.Split('/').Length - 1];
                textBox3.Text = treeView1.SelectedNode.Text;
                string repoName = treeView1.SelectedNode.FullPath.Split('\\')[0];
                string nodeForm = treeView1.SelectedNode.FullPath.Replace(treeView1.SelectedNode.Parent.FullPath, "");
                nodeForm = nodeForm.Replace("\\", "");
                textBox2.Text += "<id>*</id>" + Environment.NewLine;
                textBox2.Text += "<action>Manual</action>" + Environment.NewLine;
                textBox2.Text += $"<parameters>wget -O {textBox4.Text}{filename} https://repoDomain/repository/{repoName}/{nodeForm}</parameters>" + Environment.NewLine;
            }
        }

        private void treeView1_NodeMouseClick(object sender, TreeNodeMouseClickEventArgs e)
        {

        }

        private void treeView1_AfterCheck(object sender, TreeViewEventArgs e)
        {
            foreach (TreeNode node in treeView1.Nodes)
            {
                if (node.Checked)
                {
                    treeView1.SelectedNode = node;
                    node.Checked = false;
                }
            }
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            if (!textBox3.Text.Contains("-last-version"))
            {
                try
                {
                    int indexFirstCharWithDigit = 0;
                    if (checkBox2.Checked == true)
                    {
                        string nameOfPackage = textBox3.Text.Split('/')[textBox3.Text.Split('/').Length - 1];
                        for (int i = 0; i < nameOfPackage.Length; i++)
                        {
                            if (char.IsDigit(nameOfPackage[i])) { indexFirstCharWithDigit = i; break; }
                        }
                        //MessageBox.Show(nameOfPackage[indexFirstCharWithDigit].ToString());
                        nameOfPackage = nameOfPackage.Split('/')[nameOfPackage.Split('/').Count() - 1];
                        string replacedString = nameOfPackage.Remove(indexFirstCharWithDigit) + "-last-version";
                        textBox2.Text = textBox2.Text.Replace(nameOfPackage, replacedString);
                        textBox3.Text = replacedString;
                    }
                }
                catch { }
            }
            else { }
            checkBox2.Checked = false;
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked == true)
            {
                var lines = textBox2.Lines;
                string filename = "";
                foreach (string line in lines)
                {
                    if (line.Contains("wget") && line.Contains(textBox3.Text))
                    {
                        textBox2.Text = textBox2.Text.Replace(line, line.Replace("</parameters>", "<install></parameters>"));
                    }
                }
            }
            checkBox1.Checked = false;
        }

        private void textBox2_MouseClick(object sender, MouseEventArgs e)
        {
            foreach (string line in textBox2.Lines)
            {
                if (line.Contains("wget"))
                {
                    string new_line = line.Split(new[] { textBox4.Text }, StringSplitOptions.None)[1].Split(' ')[0];
                    textBox3.Text = new_line;
                }
            }
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {
            textBox3.Text = textBox3.Text.Split('/')[textBox3.Text.Split('/').Length - 1];
        }
    }
}

