using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using Renci.SshNet;
using System.Threading;

namespace MachineManager
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        public static SshClient ssh;
        private static ShellStream stream;
        public List<string> Modules = new List<string>();
        public int threadsCounter = 0;
        public string selectedModule = "";
        public Thread thread0;
        public Thread thread1;
        public Thread thread2;
        public Thread thread3;
        public Thread thread4;
        public Thread thread5;
        public Thread thread6;
        public Thread thread7;
        public Thread thread8;
        public Thread thread9;
        public static string login;
        public static string password;

        public void threadsCountCheck()
        {
            for (; ; )
            {
                try
                {
                    this.label3.Invoke(new MethodInvoker(delegate ()
                    {
                        this.label3.Text = string.Format("Running threads: {0}", threadsCounter);
                    }));
                }
                catch
                {
                }
            }
        }

        private void Form2_FormClosed(object sender, FormClosedEventArgs e)
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
            bool flag2 = this.thread1 != null;
            if (flag2)
            {
                try
                {
                    this.thread1.Abort();
                }
                catch
                {
                }
            }
            bool flag3 = this.thread2 != null;
            if (flag3)
            {
                try
                {
                    this.thread2.Abort();
                }
                catch
                {
                }
            }
            bool flag4 = this.thread3 != null;
            if (flag4)
            {
                try
                {
                    this.thread3.Abort();
                }
                catch
                {
                }
            }
            bool flag5 = this.thread4 != null;
            if (flag5)
            {
                try
                {
                    this.thread4.Abort();
                }
                catch
                {
                }
            }
            bool flag6 = this.thread5 != null;
            if (flag6)
            {
                try
                {
                    this.thread5.Abort();
                }
                catch
                {
                }
            }
            bool flag7 = this.thread6 != null;
            if (flag7)
            {
                try
                {
                    this.thread6.Abort();
                }
                catch
                {
                }
            }
            bool flag8 = this.thread7 != null;
            if (flag8)
            {
                try
                {
                    this.thread7.Abort();
                }
                catch
                {
                }
            }
            bool flag9 = this.thread8 != null;
            if (flag9)
            {
                try
                {
                    this.thread8.Abort();
                }
                catch
                {
                }
            }
            bool flag10 = this.thread9 != null;
            if (flag10)
            {
                try
                {
                    this.thread9.Abort();
                }
                catch
                {
                }
            }
                Application.Exit();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            button2.Enabled = false;
            button3.Enabled = false;
            button4.Enabled = false;
            button5.Enabled = false;
            button6.Enabled = false;
            button7.Enabled = false;
            button8.Enabled = false;
            button9.Enabled = false;
            button10.Enabled = false;
            button11.Enabled = false;
            button12.Enabled = false;
            button13.Enabled = false;
            textBox1.Text = Form2Helpers.getValueFromConfig(Form1.configPath +  Form1.selectedConfig, "login");
            textBox2.Text = Form2Helpers.getValueFromConfig(Form1.configPath + Form1.selectedConfig, "password");
            thread0 = new Thread(new ThreadStart(this.threadsCountCheck));
            thread0.Start();
        }
        public void streamMonitor()
        {
            this.listBox1.Invoke(new MethodInvoker(delegate ()
            {
                this.listBox1.Items.Clear();
            }));
            string sc = Form2Helpers.waitForResponseResultOut(Form2.ssh.RunCommand("rpm -qa | grep -e 'zodiac' -e 'phoenix'"));
            this.listBox1.Invoke(new MethodInvoker(delegate ()
            {
                ListBox.ObjectCollection items = this.listBox1.Items;
                object[] items2 = sc.Split(Array.Empty<char>());
                items.AddRange(items2);
            }));
            this.Modules.AddRange(sc.Split(Array.Empty<char>()));
            this.Modules.RemoveAt(this.Modules.Count<string>() - 1);
            this.listBox1.Invoke(new MethodInvoker(delegate ()
            {
                this.listBox1.Items.RemoveAt(this.listBox1.Items.Count - 1);
            }));
            foreach (object item in this.listBox1.Items)
            {
                
            }
            this.threadsCounter--;
        }

        public void connection()
        {
            try
            {
                ssh = new SshClient(this.textBox1.Text.Split(new char[]
                {
                    '@'
                })[1], this.textBox1.Text.Split(new char[]
                {
                    '@'
                })[0], this.textBox2.Text);
                button1.Invoke((MethodInvoker)(() => button1.Text = "Trying..."));
                ssh.Connect();
                button1.Invoke((MethodInvoker)(() => button1.Text = "Connect"));
                button2.Invoke((MethodInvoker)(() => button2.Enabled = true));
                button6.Invoke((MethodInvoker)(() => button6.Enabled = true));
                button7.Invoke((MethodInvoker)(() => button7.Enabled = true));
                button8.Invoke((MethodInvoker)(() => button8.Enabled = true));
                button9.Invoke((MethodInvoker)(() => button9.Enabled = true));
                button10.Invoke((MethodInvoker)(() => button10.Enabled = true));
                button11.Invoke((MethodInvoker)(() => button11.Enabled = true));
                button12.Invoke((MethodInvoker)(() => button12.Enabled = true));
                button13.Invoke((MethodInvoker)(() => button13.Enabled = true));
                MessageBox.Show("Connected!");
                button1.Invoke((MethodInvoker)(() => button1.ForeColor = Color.Lime));
            }
            catch
            {
                button1.Invoke((MethodInvoker)(() => button1.ForeColor = Color.Red));
                button1.Invoke((MethodInvoker)(() => button1.Text = "Connect"));
                MessageBox.Show("Status: Something went wrong!");
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            login = textBox1.Text;
            password = textBox2.Text;
            thread0 = new Thread(connection);
            thread0.Start();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            thread1 = new Thread(streamMonitor);
            thread1.Start();
        }
        public static void checkPid(string what, string inner)
        {
            bool complete = false;
            while (!complete)
            {
                SshCommand sshCmd = Form2.ssh.RunCommand(string.Concat(new string[]
                {
                    "ps -aux| grep -e \"",
                    what,
                    "\" -e \"",
                    inner,
                    "\""
                }));
                bool flag = sshCmd.Result.Contains(what) && sshCmd.Result.Contains(inner);
                if (!flag)
                {
                    break;
                }
                Thread.Sleep(1000);
            }
        }

        public void runSomthing(string what)
        {
            this.threadsCounter++;
            bool flag = this.Modules.Count == 0;
            if (flag)
            {
                this.streamMonitor();
            }
            string a = what;
            if (a == "update" || a == "reinstall" || a == "remove")
            {
                string command = "yum -y -v " + what + " " + this.selectedModule.Replace("\n", "");
                SshCommand sshCmd = Form2.ssh.RunCommand(command);
                bool flag2 = sshCmd.Result.Contains("Error");
                if (!flag2)
                {
                    this.listBox2.Invoke(new MethodInvoker(delegate ()
                    {
                        this.listBox2.Items.Add($"[+] [{what}] {this.selectedModule.Replace("\n", "")} - Success");
                    }));
                }
                else
                {
                    this.listBox2.Invoke(new MethodInvoker(delegate ()
                    {
                        this.listBox2.Items.Add($"[-] [{what}] {this.selectedModule.Replace("\n", "")} - Error");
                    }));
                }
            }
            this.threadsCounter--;
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            button3.Enabled = true;
            button4.Enabled = true;
            button5.Enabled = true;
            bool flag = this.listBox1.SelectedItem != null;
            if (flag)
            {
                this.selectedModule = this.listBox1.SelectedItem.ToString();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            thread2 = new Thread(() => runSomthing("update"));
            thread2.Start();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            thread2 = new Thread(() => runSomthing("reinstall"));
            thread2.Start();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            DialogResult msg = MessageBox.Show("Really?", "Warning", MessageBoxButtons.YesNo, MessageBoxIcon.Exclamation, MessageBoxDefaultButton.Button2);
            bool flag = msg == DialogResult.Yes;
            if (flag)
            {
                this.threadsCounter++;
                this.thread4 = new Thread(delegate ()
                {
                    this.runSomthing("remove");
                });
                this.thread4.Start();
            }
            bool flag2 = msg != DialogResult.No;
            if (flag2)
            {
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            nexusTake form3 = new nexusTake();
            form3.Show();
        }
        public void waitForResponse(SshCommand sshCmd)
        {
            bool flag = sshCmd.Result.Contains("Error");
            if (!flag)
            {
                this.listBox2.Invoke(new MethodInvoker(delegate ()
                {
                    this.listBox2.Items.Add("[+] Taking output");
                }));
            }
            else
            {
                this.listBox2.Invoke(new MethodInvoker(delegate ()
                {
                    this.listBox2.Items.Add("[-] Error in " + sshCmd.CommandText);
                }));
            }
        }

        public void restartAllServices()
        {
            this.threadsCounter++;
            bool flag = this.listBox1.Items.Contains("zodiac");
            if (flag)
            {
                this.waitForResponse(Form2.ssh.RunCommand("sudo systemctl resart zodiacd"));
                this.waitForResponse(Form2.ssh.RunCommand("sudo systemctl resart zodiac*"));
            }
            bool flag2 = this.listBox1.Items.Contains("phoenix");
            if (flag2)
            {
                this.waitForResponse(Form2.ssh.RunCommand("sudo systemctl resart phoenixd"));
                this.waitForResponse(Form2.ssh.RunCommand("sudo systemctl resart phoenix*"));
            }
            this.waitForResponse(Form2.ssh.RunCommand("sudo systemctl resart bpm-app"));
            this.waitForResponse(Form2.ssh.RunCommand("sudo systemctl resart dms*"));
            this.waitForResponse(Form2.ssh.RunCommand("sudo systemctl resart dmsd"));
            this.waitForResponse(Form2.ssh.RunCommand("sudo systemctl resart dms-app"));
            this.threadsCounter--;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            thread2 = new Thread(restartAllServices);
            thread2.Start();
        }
        public void camundaZodiac()
        {
            this.threadsCounter++;
            List<string> apache_conf = new List<string>();
            List<string> usrLocalBpm = new List<string>();
            this.waitForResponse(Form2.ssh.RunCommand("cd /home/avalon/"));
            this.waitForResponse(Form2.ssh.RunCommand("mkdir /home/avalon/camunda"));
            this.waitForResponse(Form2.ssh.RunCommand("cd /home/avalon/camunda"));
            string command = "wget -O /home/avalon/camunda/camunda.zip https://downloads.camunda.cloud/release/camunda-bpm/tomcat/7.10/camunda-bpm-tomcat-7.10.0.zip";
            this.waitForResponse(Form2.ssh.RunCommand(command));
            this.waitForResponse(Form2.ssh.RunCommand("unzip /home/avalon/camunda/camunda.zip -d /home/avalon/camunda/"));
            SftpClient client = new SftpClient(this.textBox1.Text.Split(new char[]
            {
                '@'
            })[1], 22, this.textBox1.Text.Split(new char[]
            {
                '@'
            })[0], this.textBox2.Text);
            client.Connect();
            apache_conf.Add(Directory.GetCurrentDirectory() + "\\config_files\\bpm-platform.xml");
            apache_conf.Add(Directory.GetCurrentDirectory() + "\\config_files\\server.xml");
            apache_conf.Add(Directory.GetCurrentDirectory() + "\\config_files\\web.xml");
            client.ChangeDirectory("/home/avalon/camunda/server/apache-tomcat-9.0.12/conf/");
            foreach (string file in apache_conf)
            {
                using (FileStream fileStream = new FileStream(file, FileMode.Open))
                {
                    client.BufferSize = 4096U;
                    client.UploadFile(fileStream, Path.GetFileName(file), null);
                }
            }
            this.waitForResponse(Form2.ssh.RunCommand("sudo rm -rf /home/avalon/server/apache*/webapps/camunda-invoice"));
            this.waitForResponse(Form2.ssh.RunCommand("su - avalon -c \"mysql -uroot -planlot < /usr/local/bpm/support/zodiac_camunda.sql\""));
            this.waitForResponse(Form2.ssh.RunCommand("su - avalon -c \"mysql -uroot -planlot camundabpm < /home/avalon/camunda/sql/create/mysql_identity*.sql\""));
            this.waitForResponse(Form2.ssh.RunCommand("su - avalon -c \"mysql -uroot -planlot camundabpm < /home/avalon/camunda/sql/create/mysql_engine*.sql\""));
            this.waitForResponse(Form2.ssh.RunCommand("su - avalon -c \"mysql -uroot -planlot camundabpm < /usr/local/bpm/support/mysql_zodiac.sql\""));
            this.waitForResponse(Form2.ssh.RunCommand("yum -y -v install java"));
            client.ChangeDirectory("/home/avalon/camunda/");
            this.waitForResponse(Form2.ssh.RunCommand("wget http://ftp.iij.ad.jp/pub/db/mysql/Downloads/Connector-J/mysql-connector-java-8.0.15.zip"));
            this.waitForResponse(Form2.ssh.RunCommand("unzip mysql-connector-java-8.0.15.zip -d /home/avalon/camunda/mysql-connector/"));
            this.waitForResponse(Form2.ssh.RunCommand("sudo cp /home/avalon/camunda/mysql-connector/mysql-*/mysql-connector-java-8.0.15.jar /home/avalon/camunda/server/apache-tomcat*/lib/ "));
            this.waitForResponse(Form2.ssh.RunCommand("sudo cp /usr/local/bpm/bpm/libs/auth-filter/target/zbpm-auth-filter* /home/avalon/camunda/server/apache-tomcat*/webapps/engine-rest/WEB-INF/lib/"));
            this.waitForResponse(Form2.ssh.RunCommand("sudo cp /usr/local/bpm/bpm/libs/auth-filter/target/alternateLocation/gson* /home/avalon/camunda/server/apache-tomcat*/webapps/engine-rest/WEB-INF/lib/"));
            this.threadsCounter--;
            client.ChangeDirectory("/usr/local/bpm/conf/");
            usrLocalBpm.Add(Directory.GetCurrentDirectory() + "\\config_files\\bpm_camunda.json");
            usrLocalBpm.Add(Directory.GetCurrentDirectory() + "\\config_files\\mysql_bpm_camunda.json");
            foreach (string file2 in usrLocalBpm)
            {
                using (FileStream fileStream2 = new FileStream(file2, FileMode.Open))
                {
                    client.BufferSize = 4096U;
                    client.UploadFile(fileStream2, Path.GetFileName(file2), null);
                }
            }
            this.threadsCounter--;
        }
        private void button8_Click(object sender, EventArgs e)
        {
            thread2 = new Thread(camundaZodiac);
            thread2.Start();
        }

        public void updateModules()
        {
            this.threadsCounter++;
            foreach (string item in listBox1.Items)
            {
                this.listBox2.Invoke(new MethodInvoker(delegate ()
                {
                    this.listBox2.Items.Add(string.Format("[+] Update this module -> {0}", item));
                }));
                this.waitForResponse(Form2.ssh.RunCommand(string.Format("sudo yum -y -v update {0}", item)));
                this.listBox2.Invoke(new MethodInvoker(delegate ()
                {
                    this.listBox2.Items.Add(string.Format("[+] End sub task -> {0}", item));
                }));
            }
            this.listBox2.Invoke(new MethodInvoker(delegate ()
            {
                this.listBox2.Items.Add("[+] End update task ");
            }));
            this.threadsCounter--;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            thread2 = new Thread(updateModules);
            thread2.Start();
        }

        public void camundaMove(string choose)
        {
            this.threadsCounter++;
            if (!(choose == "start"))
            {
                if (!(choose == "stop"))
                {
                    if (choose == "restart")
                    {
                        this.camundaMove("stop");
                        this.camundaMove("start");
                    }
                }
                else
                {
                    this.waitForResponse(Form2.ssh.RunCommand("/home/avalon/camunda/server/apache*/bin/shutdown.sh"));
                }
            }
            else
            {
                this.waitForResponse(Form2.ssh.RunCommand("/home/avalon/camunda/server/apache*/bin/startup.sh"));
            }
            this.threadsCounter--;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            thread3 = new Thread(()=> camundaMove("start"));
            thread2.Start();
        }

        private void button11_Click(object sender, EventArgs e)
        {
            thread3 = new Thread(() => camundaMove("restart"));
            thread2.Start();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            thread3 = new Thread(() => camundaMove("stop"));
            thread2.Start();
        }

        public void installDms()
        {
            this.threadsCounter++;
            this.waitForResponse(Form2.ssh.RunCommand("yum -y -v install mongodb"));
            this.waitForResponse(Form2.ssh.RunCommand("sudo systemctl resart dms*"));
            this.waitForResponse(Form2.ssh.RunCommand("sudo systemctl resart dmsd"));
            this.waitForResponse(Form2.ssh.RunCommand("sudo systemctl resart dms-app"));
            this.threadsCounter--;
        }
        private void button13_Click(object sender, EventArgs e)
        {
            this.thread9 = new Thread(delegate ()
            {
                this.installDms();
            });
            this.thread9.Start();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            
        }

        private void button15_Click(object sender, EventArgs e)
        {
            Form3 form3 = new Form3();
            form3.Show();
        }
    }
}
