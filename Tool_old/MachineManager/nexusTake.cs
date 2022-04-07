using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading;
using System.Windows.Forms;
using Renci.SshNet;

namespace MachineManager
{
    public partial class nexusTake : Form
    {
        public nexusTake()
        {
            InitializeComponent();
        }

		private List<string> reposNames = new List<string>();
		public Thread thread0;
		public static List<string> listWithCheckedItems = new List<string>();
		//private IContainer components = null;

		public static string waitForResponse(SshCommand sshCmd)
        {
            return sshCmd.Result;
        }

        private void button1_Click(object sender, EventArgs e)
        {
			this.thread0 = new Thread(new ThreadStart(this.downloadingNeededModules));
			this.thread0.Start();
		}

		public void downloadingNeededModules()
		{
			foreach (object item in this.checkedListBox1.CheckedItems)
			{
				List<string> links = new List<string>();
				string json = "{'action':'coreui_Browse','method':'read','data':[{'repositoryName':'" + item.ToString() + "','node':'master'}],'type':'rpc','tid':6}";
				byte[] body = Encoding.UTF8.GetBytes(json);
				HttpWebRequest request = (HttpWebRequest)WebRequest.Create("https://nexus.link-to.ru/service/extdirect");
				request.Method = "POST";
				request.ContentType = "application/json";
				request.ContentLength = (long)body.Length;
				Stream stream = request.GetRequestStream();
				stream.Write(body, 0, body.Length);
				stream.Close();
				HttpWebResponse response = (HttpWebResponse)request.GetResponse();
				string responseString = new StreamReader(response.GetResponseStream()).ReadToEnd();
				this.label1.Invoke(new MethodInvoker(delegate ()
				{
					this.label1.Text = "Final request";
				}));
				for (int i = 0; i < responseString.Split(new string[]
				{
					"\"id\":"
				}, StringSplitOptions.None).Count<string>(); i++)
				{
					try
					{
						string repo = responseString.Split(new string[]
						{
							"\"id\":"
						}, StringSplitOptions.None)[i + 1];
						string addedItem = repo.Split(new string[]
						{
							"\""
						}, StringSplitOptions.None)[1].Split(new string[]
						{
							"\", \"text\":"
						}, StringSplitOptions.None)[0];
						bool flag = !addedItem.Contains("\"");
						if (flag)
						{
							links.Add(addedItem);
						}
					}
					catch
					{
					}
				}
				string lastVersionOfmaster = "";
				double date = 0.0;
				foreach (string link in links)
				{
					try
					{
						bool flag2 = date < double.Parse(link.Split(new char[]
						{
							'.'
						})[link.Split(new char[]
						{
							'.'
						}).Count<string>() - 5]);
						if (flag2)
						{
							date = double.Parse(link.Split(new char[]
							{
								'.'
							})[link.Split(new char[]
							{
								'.'
							}).Count<string>() - 5]);
							lastVersionOfmaster = link;
						}
					}
					catch
					{
					}
				}
				string urlLink = string.Format("https://nexus.link-to.ru/repository/{0}/{1}", item, lastVersionOfmaster);
				nexusTake.waitForResponse(Form2.ssh.RunCommand("mkdir /root/modules/"));
				string pochemuTiNeRabotaesh = lastVersionOfmaster.Replace("master/", "");
				this.label1.Invoke(new MethodInvoker(delegate ()
				{
					this.label1.Text = "Wget start downloading";
				}));
				string output = nexusTake.waitForResponse(Form2.ssh.RunCommand("wget -q -O /root/modules/" + pochemuTiNeRabotaesh + " " + urlLink));
				this.label1.Invoke(new MethodInvoker(delegate ()
				{
					this.label1.Text = "Ready";
				}));
				nexusTake.waitForResponse(Form2.ssh.RunCommand("yum -y -v install /root/modules/" + pochemuTiNeRabotaesh));
			}
		}

		private void Form3_Load(object sender, EventArgs e)
        {
			this.button1.Text = "Install modules";
			this.label1.Text = "Status";
			this.Text = "nexusTake";
			this.treeView1.CheckBoxes = true;

			//this.sameRequestsLoadPage();
			string json = "{ 'action':'coreui_Repository','method':'readReferences','data':[{ 'page':1,'start':0,'limit':25}],'type':'rpc','tid':3}";
			byte[] body = Encoding.UTF8.GetBytes(json);
			HttpWebRequest request = (HttpWebRequest)WebRequest.Create("https://nexus.link-to.ru/service/extdirect");
			request.Method = "POST";
			request.ContentType = "application/json";
			request.ContentLength = (long)body.Length;
			Stream stream = request.GetRequestStream();
			stream.Write(body, 0, body.Length);
			stream.Close();
			HttpWebResponse response = (HttpWebResponse)request.GetResponse();
			string responseString = new StreamReader(response.GetResponseStream()).ReadToEnd();
			for (int i = 0; i < responseString.Split(new string[]
			{
				"repositoryName"
			}, StringSplitOptions.None).Count<string>(); i++)
			{
				string repo = responseString.Split(new string[]
				{
					"repositoryName"
				}, StringSplitOptions.None)[i];
				string addedItem = repo.Split(new string[]
				{
					"\":\""
				}, StringSplitOptions.None)[1].Split(new string[]
				{
					"\",\"online\":"
				}, StringSplitOptions.None)[0];
				bool flag = !addedItem.Contains("\"");
				if (flag)
				{
					this.reposNames.Add(addedItem);
					this.checkedListBox1.Items.Add(addedItem);
					this.treeView1.Nodes.Add(addedItem);
				}
			}
		}

        private void checkedListBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
			
		}

        private void nexusTake_FormClosing(object sender, FormClosingEventArgs e)
        {
			bool flag = this.thread0 != null;
			if (flag)
			{
				try
				{
					this.thread0.Abort();
				}
				catch
				{
				}
			}
		}

        private void checkedListBox1_MouseClick(object sender, MouseEventArgs e)
        {
			this.checkedListBox1.SetItemChecked(this.checkedListBox1.SelectedIndex, true);
		}

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
			foreach (object obj in this.checkedListBox1.CheckedItems)
			{
				string item = (string)obj;
				bool flag = !nexusTake.listWithCheckedItems.Contains(item);
				if (flag)
				{
					nexusTake.listWithCheckedItems.Add(item);
				}
			}
			this.checkedListBox1.Items.Clear();
			foreach (string item2 in this.reposNames)
			{
				bool flag2 = item2.Contains(this.textBox1.Text);
				if (flag2)
				{
					bool flag3 = nexusTake.listWithCheckedItems.Contains(item2);
					if (flag3)
					{
						this.checkedListBox1.Items.Add(item2, true);
					}
					else
					{
						this.checkedListBox1.Items.Add(item2);
					}
				}
			}
			bool flag4 = this.textBox1.Text.Length == 0;
			if (flag4)
			{
				nexusTake.listWithCheckedItems.Clear();
			}
		}

        private void treeView1_NodeMouseClick(object sender, TreeNodeMouseClickEventArgs e)
        {
			
		}

		List<string> nexusPaths = new List<string>();
		List<string> nexusProjects = new List<string>();

		public TreeNodeCollection getDatatFromStorage(TreeView treeNode, int nexusPathIndex)
        {
			string json0 = "{'action':'coreui_Browse','method':'read','data':[{'repositoryName': '" + treeNode.SelectedNode.Text + "','node':'" + nexusPaths[nexusPathIndex] + "'}],'type':'rpc','tid':6}";
			byte[] body0 = Encoding.UTF8.GetBytes(json0);
			HttpWebRequest request0 = (HttpWebRequest)WebRequest.Create("https://nexus.link-to.ru/service/extdirect");
			request0.Method = "POST";
			request0.ContentType = "application/json";
			request0.ContentLength = (long)body0.Length;
			Stream stream0 = request0.GetRequestStream();
			stream0.Write(body0, 0, body0.Length);
			stream0.Close();
			int id = 0;
			treeNode.Invoke((MethodInvoker)(() => id = treeNode.SelectedNode.Index));
			HttpWebResponse response0 = (HttpWebResponse)request0.GetResponse();
			string responseString0 = new StreamReader(response0.GetResponseStream()).ReadToEnd();
			for (int j = 0; j < responseString0.Split('\"').Length; j++)
			{
				if (responseString0.Split('\"')[j].Contains("id") && responseString0.Split('\"')[j + 1].Contains(":"))
				{
					int count = treeView1.Nodes[id].Nodes.Count - 1;
					treeView1.Invoke((MethodInvoker)(() => treeView1.Nodes[id].Nodes[count].Nodes.Add(responseString0.Split('\"')[j + 2])));
				}
			}
			return treeNode.Nodes;
        }

		public TreeView getBranches(TreeView treeNode)
        {
			int id = 0;
			string name = "";
			treeNode.Invoke((MethodInvoker)(() => id = treeNode.SelectedNode.Index));
			treeNode.Invoke((MethodInvoker)(() => name = treeNode.SelectedNode.Text));
            string json = "{'action':'coreui_Browse','method':'read','data':[{'repositoryName': '" + name + "','node':'/'}],'type':'rpc','tid':6}";
            byte[] body = Encoding.UTF8.GetBytes(json);
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create("https://nexus.link-to.ru/service/extdirect");
            request.Method = "POST";
            request.ContentType = "application/json";
            request.ContentLength = (long)body.Length;
            Stream stream = request.GetRequestStream();
            stream.Write(body, 0, body.Length);
            stream.Close();
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            string responseString = new StreamReader(response.GetResponseStream()).ReadToEnd();
			for (int i = 0; i < responseString.Split('\"').Length; i++)
            {
				if (responseString.Split('\"')[i].Contains("id") && responseString.Split('\"')[i + 1].Contains(":"))
				{
					treeView1.Invoke((MethodInvoker)(() => treeView1.Nodes[id].Nodes.Add(responseString.Split('\"')[i + 2])));
					nexusProjects.Add(responseString.Split('\"')[i + 2]);
				}
			}
			return treeNode;
		}

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
			nexusPaths.Add("/");
			if (treeView1.SelectedNode.Checked == false)
            {
				treeView1.SelectedNode.Checked = true;
			}
            else
            {
				treeView1.SelectedNode.Checked = false;
			}
			int id = treeView1.SelectedNode.Index;
			string name = treeView1.SelectedNode.Text;
			getBranches(treeView1);
			MessageBox.Show(nexusPaths.Count().ToString());
			//while (int i = 0;  !nexusPaths[i].Contains(".rpm"))
   //         {
			//	getDatatFromStorage(treeView1, i);
			//}

        }
    }
}
