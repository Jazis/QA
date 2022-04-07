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
using System.Threading;
using Renci.SshNet;

namespace MachineManager
{
    public partial class Form3 : Form
    {
        public static string scenarioPath;
        public static string selectedScenario;
        public static List<string> itemsOfCombobox = new List<string>();
        public static List<string> customPaths = new List<string>();
        public static string[] cpaths;
        public static int selectedRow = 0;
        public Form3()
        {
            InitializeComponent();
        }

        public void backgroundChecker()
        {
            while(true)
            {
                
            }
        }

        private void Form3_Load(object sender, EventArgs e)
        {
            foreach(string line in File.ReadAllLines(Form1.configPath + Form1.selectedConfig))
            {
                string line0;
                if (line.Split('=')[1][0].ToString() == " ") { line0 = line.Replace(line.Split('=')[1][0].ToString(), ""); }
                else { line0 = line; }
                if (line0.Split('=')[1][0].ToString() == "/" && line0.Split('=')[1][line0.Split('=')[1].Length-1].ToString() == "/")
                {
                    customPaths.Add(line0.Split('=')[0] + " " + line0.Split('=')[1]);
                }
            }
            comboBox2.Items.Clear();
            comboBox2.Items.Add("Service status");
            comboBox2.Items.Add("Service status2");
            comboBox2.Items.Add("Manual");
            comboBox2.Items.Add("File upload");
            foreach (string item in comboBox2.Items)
            {
                itemsOfCombobox.Add(item.ToString());
            } 
            scenarioPath = Directory.GetCurrentDirectory() + "\\scenarios\\";
            foreach (var filename in Directory.GetFiles(scenarioPath))
            {
                if (filename.Contains(".scenario") || filename.Contains(".json"))
                {
                    comboBox1.Items.Add(filename.Split(new[] { "\\" }, StringSplitOptions.None)[filename.Split(new[] { "\\" }, StringSplitOptions.None).Length - 1]);
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text == "Change")
            {
                try { dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Cells[1].Value = comboBox2.SelectedItem.ToString(); } 
                catch { dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Cells[1].Value = comboBox2.Text.ToString(); }
                dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Cells[2].Value = textBox1.Text;
                button1.Text = "Add";
            }
            else
            {
                int lastRow = dataGridView1.Rows.Count;
                dataGridView1.Rows.Add(lastRow, comboBox2.Text, textBox1.Text);
            }

        }

        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBox2.SelectedItem != null)
            {
                comboBox2.Text = comboBox2.SelectedItem.ToString();
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            textBox2.Text = comboBox1.Text;
            dataGridView1.Rows.Clear();
            selectedScenario = comboBox1.Text;
            string id = "", action ="", parameters = "";
            foreach (string line in File.ReadLines(scenarioPath + selectedScenario))
            {
                if (selectedScenario.Contains(".scenario"))
                {
                    if (line.Contains("<id>"))
                    {
                        id = line.Split(new[] { "<id>" }, StringSplitOptions.None)[1].Split(new[] { "</id>" }, StringSplitOptions.None)[0];
                    }
                    if (line.Contains("<action>"))
                    {
                        action = line.Split(new[] { "<action>" }, StringSplitOptions.None)[1].Split(new[] { "</action>" }, StringSplitOptions.None)[0];
                    }
                    if (line.Contains("<parameters>"))
                    {
                        parameters = line.Split(new[] { "<parameters>" }, StringSplitOptions.None)[1].Split(new[] { "</parameters>" }, StringSplitOptions.None)[0];
                    }
                    if (id != "" && action != "" && parameters != "")
                    {
                        dataGridView1.Rows.Add(id, action, parameters);
                        id = ""; action = ""; parameters = "";
                    }
                }
                if (selectedScenario.Contains(".json"))
                {
                    string nline = line.Replace("{ \"data\" : {", string.Empty);
                    foreach(string row in nline.Split(new[] { "\"}"}, StringSplitOptions.None))
                    {
                        if (row.Contains(":"))
                        {
                            string row0 = row.Replace("}}", "");
                            string rowNumber = row0.Split(':')[0].Replace("\"", "").Replace(",", "").Trim();
                            string rowAction = row.Split(':')[2].Replace(", \"parameters\"", string.Empty).Replace("\"", string.Empty).Replace("\",", string.Empty);
                            string rowParams = row.Split(':')[3].Replace(row.Split(':')[3][0].ToString(), "").Remove(0, 1); //.Replace(row.Split(':')[3][row.Split(':')[3].Length - 1].ToString(), "");
                            dataGridView1.Rows.Add(rowNumber, rowAction, rowParams);
                        }
                    }
                }
            }
        }

        public void saveFile(string filePath)
        {
            try
            {
                File.Delete(filePath);
            } catch { }
            StreamWriter streamWriter = new StreamWriter(filePath);
            int lastLine = dataGridView1.Rows.Count - 1;
            selectedScenario = filePath.Split('.')[filePath.Split('.').Length - 1];
            if (selectedScenario.Contains("json")) { streamWriter.Write("{ \"data\" : {"); }
            for (int i = 0; i < dataGridView1.Rows.Count; i++)
            {
                if (selectedScenario.Contains("scenario"))
                {
                    if (dataGridView1.Rows[i].Cells[0].Value != null && dataGridView1.Rows[i].Cells[1].Value != null && dataGridView1.Rows[i].Cells[2].Value != null)
                    {
                        streamWriter.WriteLine("<id>" + dataGridView1.Rows[i].Cells[0].Value + "</id>");
                        streamWriter.WriteLine("\t<action>" + dataGridView1.Rows[i].Cells[1].Value + "</action>");
                        streamWriter.WriteLine("\t<parameters>" + dataGridView1.Rows[i].Cells[2].Value + "</parameters>");
                    }
                }
                if (selectedScenario.Contains("json"))
                {
                    if (dataGridView1.Rows[i].Cells[0].Value != null && dataGridView1.Rows[i].Cells[1].Value != null && dataGridView1.Rows[i].Cells[2].Value != null)
                    {
                        streamWriter.Write("\"" + dataGridView1.Rows[i].Cells[0].Value + "\" : {");
                        streamWriter.Write("\"action\" : \"" + dataGridView1.Rows[i].Cells[1].Value + "\", ");
                        streamWriter.Write("\"parameters\" : \"");
                        foreach (char c in dataGridView1.Rows[i].Cells[2].Value.ToString())
                        {
                            if (Char.IsSymbol(c)) { streamWriter.Write("\\" + c); } else { streamWriter.Write(c); }
                        }
                        streamWriter.Write("\"");
                        if (lastLine-1 == i) { }
                        else { streamWriter.Write("}, "); }
                    }
                }
            }
            if (selectedScenario.Contains(".json")) 
            {
                streamWriter.Write("}}}");
            }    
            streamWriter.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (textBox2.Text == string.Empty)
            {
                MessageBox.Show("Please, input filename!");
            }
            else
            {
                if (File.Exists(scenarioPath + textBox2.Text))
                {
                    DialogResult dialog = MessageBox.Show("File already exist! Rewrite?", "Warning", MessageBoxButtons.YesNo, MessageBoxIcon.Warning, MessageBoxDefaultButton.Button1);
                    if (dialog == DialogResult.Yes)
                    {
                        saveFile(scenarioPath + textBox2.Text);
                        MessageBox.Show("File sucessfully saved! " + textBox2.Text);

                    }
                    if (dialog == DialogResult.No) { }
                }
                if (textBox2.Text == string.Empty)
                {
                    MessageBox.Show("Please, input filename!", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                if (textBox2.Text != string.Empty)
                {
                    if (!textBox2.Text.Contains(".scenario") || !textBox2.Text.Contains(".json"))
                    {
                        saveFile(scenarioPath + textBox2.Text + ".scenario");
                        MessageBox.Show("File sucessfully saved! " + textBox2.Text + ".scenario");
                    }
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (this.dataGridView1.SelectedRows.Count > 0)
            {
                dataGridView1.Rows.RemoveAt(this.dataGridView1.SelectedRows[0].Index);
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (this.dataGridView1.SelectedRows.Count > 0)
            {
                List<string> list = new List<string>();
                int selectedRowIndex = dataGridView1.SelectedRows[0].Index;
                var selectedLine = dataGridView1.Rows[dataGridView1.SelectedRows[0].Index];
                //list.Add(dataGridView1.Rows[selectedRowIndex - 1].Cells[0].Value.ToString());
                list.Add(dataGridView1.Rows[selectedRowIndex - 1].Cells[1].Value.ToString());
                list.Add(dataGridView1.Rows[selectedRowIndex - 1].Cells[2].Value.ToString());
                //dataGridView1.Rows[selectedRowIndex - 1].Cells[0].Value = selectedLine.Cells[0].Value;
                dataGridView1.Rows[selectedRowIndex - 1].Cells[1].Value = selectedLine.Cells[1].Value;
                dataGridView1.Rows[selectedRowIndex - 1].Cells[2].Value = selectedLine.Cells[2].Value;
                //selectedLine.Cells[0].Value = list[0];
                selectedLine.Cells[1].Value = list[0];
                selectedLine.Cells[2].Value = list[1];
                dataGridView1.Refresh();
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (this.dataGridView1.SelectedRows.Count > 0)
            {
                List<string> list = new List<string>();
                int selectedRowIndex = dataGridView1.SelectedRows[0].Index;
                var selectedLine = dataGridView1.Rows[dataGridView1.SelectedRows[0].Index];
                //list.Add(dataGridView1.Rows[selectedRowIndex + 1].Cells[0].Value.ToString());
                list.Add(dataGridView1.Rows[selectedRowIndex + 1].Cells[1].Value.ToString());
                list.Add(dataGridView1.Rows[selectedRowIndex + 1].Cells[2].Value.ToString());
                //dataGridView1.Rows[selectedRowIndex + 1].Cells[0].Value = selectedLine.Cells[0].Value;
                dataGridView1.Rows[selectedRowIndex + 1].Cells[1].Value = selectedLine.Cells[1].Value;
                dataGridView1.Rows[selectedRowIndex + 1].Cells[2].Value = selectedLine.Cells[2].Value;
                //selectedLine.Cells[0].Value = list[0];
                selectedLine.Cells[1].Value = list[0];
                selectedLine.Cells[2].Value = list[1];
                dataGridView1.Refresh();
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            if (dataGridView1.SelectedCells[0].RowIndex != comboBox2.Items.Count - 1)
            {
                dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Selected = true;
                comboBox2.SelectedItem = dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Cells[1].Value;
                textBox1.Text = dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Cells[2].Value.ToString();
                if (selectedRow == dataGridView1.SelectedCells[0].RowIndex)
                {
                    button1.Text = "Change";
                }
                else
                {
                    button1.Text = "Add";
                    selectedRow = dataGridView1.SelectedCells[0].RowIndex;
                }
            }

            //try
            //{
            //    //dataGridView1.SelectedCells[0].RowIndex
            //    dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Selected = true;
            //    comboBox2.SelectedItem = dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Cells[1].Value;
            //    textBox1.Text = dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Cells[2].Value.ToString();
            //    if (button1.Text == "Change") { button1.Text = "Add"; }
            //    else { button1.Text = "Change"; }
            //}
            //catch { }
        }

        public void runScenario()
        {
            for (int i = 0; i < dataGridView1.Rows.Count; i++)
            {
                dataGridView1.Rows[i].DefaultCellStyle.BackColor = Color.White;
                foreach(string line in customPaths)
                {
                    if (dataGridView1.Rows[i].Cells[0].Value != null && dataGridView1.Rows[i].Cells[1].Value != null && dataGridView1.Rows[i].Cells[2].Value != null)
                    {
                        if (dataGridView1.Rows[i].Cells[2].Value.ToString().Contains("{" + line.Split(new[] { "] " }, StringSplitOptions.None)[0].Replace('['.ToString(), "") + "}"))
                        {
                            var tempBefore = dataGridView1.Rows[i].Cells[2].Value.ToString().Split('{')[0];
                            var tempAfter = dataGridView1.Rows[i].Cells[2].Value.ToString().Split('}')[1];
                            dataGridView1.Rows[i].Cells[2].Value = tempBefore + line.Split(new[] { "] " }, StringSplitOptions.None)[1] + tempAfter;
                        }
                    }
                }
                
            }
            for(int i = 0; i< dataGridView1.Rows.Count; i++)
            {
                if (dataGridView1.Rows[i].Cells[0].Value != null && dataGridView1.Rows[i].Cells[1].Value != null && dataGridView1.Rows[i].Cells[2].Value != null)
                {
                    if (dataGridView1.Rows[i].Cells[1].Value.ToString().Contains("Service status"))
                    {
                        string output = Form2Helpers.waitForResponseResultOut(Form2.ssh.RunCommand("sudo systemctl status " + dataGridView1.Rows[i].Cells[2].Value.ToString() + " -l"));
                        textBox3.Invoke((MethodInvoker)(() => textBox3.Text += output));
                        dataGridView1.Rows[i].DefaultCellStyle.BackColor = Color.Green;
                    }
                    if (dataGridView1.Rows[i].Cells[1].Value.ToString().Contains("Manual"))
                    {
                        string output = Form2Helpers.waitForResponseResultOut(Form2.ssh.RunCommand(dataGridView1.Rows[i].Cells[2].Value.ToString()));

                        textBox3.Invoke((MethodInvoker)(() => textBox3.Text += output));
                        dataGridView1.Rows[i].DefaultCellStyle.BackColor = Color.Green;
                    }
                    if (dataGridView1.Rows[i].Cells[1].Value.ToString().Contains("Wget"))
                    {
                        string output = Form2Helpers.waitForResponseResultOut(Form2.ssh.RunCommand("wget " + dataGridView1.Rows[i].Cells[2].Value.ToString()));

                        textBox3.Invoke((MethodInvoker)(() => textBox3.Text += output));
                        dataGridView1.Rows[i].DefaultCellStyle.BackColor = Color.Green;
                    }
                    if (dataGridView1.Rows[i].Cells[1].Value.ToString().Contains("File upload"))
                    {
                        SftpClient client = Form2Helpers.sftpConnect();
                        var directory = client.WorkingDirectory;
                        client.ChangeDirectory(dataGridView1.Rows[i].Cells[2].Value.ToString().Split(':')[0]);
                        string file;
                        if (dataGridView1.Rows[i].Cells[2].Value.ToString().Contains("{softDir}"))
                        {
                            file = Directory.GetCurrentDirectory() + dataGridView1.Rows[i].Cells[2].Value.ToString().Split(new[] { "{softDir}" }, StringSplitOptions.None)[1];
                        }
                        else
                        {
                            file = dataGridView1.Rows[i].Cells[2].Value.ToString().Replace(dataGridView1.Rows[i].Cells[2].Value.ToString().Split(':')[0], "").Remove(0, 1);
                        }
                        using (FileStream fileStream = new FileStream(file, FileMode.Open))
                        {
                            client.BufferSize = 4096U;
                            client.UploadFile(fileStream, Path.GetFileName(file), null);
                        }
                        client.ChangeDirectory(directory);
                        dataGridView1.Rows[i].DefaultCellStyle.BackColor = Color.Green;
                        //string output = Form2Helpers.waitForResponseResultOut(Form2.ssh.RunCommand(dataGridView1.Rows[i].Cells[2].Value.ToString()));

                        //textBox3.Invoke((MethodInvoker)(() => textBox3.Text += output));
                    }
                }
            }
            MessageBox.Show("Scenario complete!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
            //Form2Helpers.waitForResponseResultOut(Form2.ssh.RunCommand("sudo systemctl resart zodiacd"));
        }

        private void button6_Click(object sender, EventArgs e)
        {
            textBox3.Text = "";
            Thread thread = new Thread(runScenario);
            thread.Start();
        }

        private void comboBox2_TextChanged(object sender, EventArgs e)
        {
            comboBox2.DroppedDown = true;
            int counter = 0;
            comboBox2.Items.Clear();
            foreach (string item in itemsOfCombobox)
            {
                if (item.ToString().Contains(comboBox2.Text))
                {
                    comboBox2.Items.Add(item);
                    counter++;
                }
                comboBox2.SelectionStart = comboBox2.Text.Length;
                comboBox2.SelectionLength = 0;
            }
            if (counter == 1) { comboBox2.DroppedDown = false; }
            else { comboBox2.DroppedDown = true; }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string path = Directory.GetCurrentDirectory() + "\\help\\0.txt";
            string path0 = path.ToString();
            string text = "File upload\n\tExample of params: <path on remote computer>:<path to file>";
            MessageBox.Show(text, "Help", 0, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1, 0, path);
        }

        private void comboBox2_KeyUp(object sender, KeyEventArgs e)
        {
        }

        private void comboBox2_KeyDown(object sender, KeyEventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
            dataGridView1.Rows.Clear();
            comboBox1.Text = "";
        }
    }
}
