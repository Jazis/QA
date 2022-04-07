using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Windows.Forms;

namespace ScenarioMaker
{
    public partial class Form1 : Form
    {
        public static string scenarioPath;
        public static string descriptionPath;
        public static string selectedScenario;
        public static List<string> itemsOfCombobox = new List<string>();
        public static List<string> customPaths = new List<string>();
        public static string[] cpaths;
        public static string new_chain = "";
        public static string command_text = "";

        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            dataGridView1.Columns[0].FillWeight = 15;
            comboBox2.Items.Clear();
            comboBox2.Items.Add("Service status");
            comboBox2.Items.Add("Manual");
            comboBox2.Items.Add("Get license");
            comboBox2.Items.Add("Make backup");
            comboBox2.Items.Add("Wget");
            comboBox2.Items.Add("Unzip");
            comboBox2.Items.Add("Edit");
            comboBox2.Items.Add("Kill process");
            foreach (string item in comboBox2.Items)
            {
                itemsOfCombobox.Add(item.ToString());
            }
            scenarioPath = Directory.GetCurrentDirectory() + "\\scenarios\\";
            //descriptionPath = Directory.GetCurrentDirectory() + "\\descriptions\\";
            //if (!Directory.Exists(descriptionPath))
            //{
            //    Directory.CreateDirectory(descriptionPath);
            //}
            if (!Directory.Exists(scenarioPath))
            {
                Directory.CreateDirectory(scenarioPath);
            }
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
                catch (System.NullReferenceException) { }
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
            if (comboBox2.Text.Contains("Get license"))
            {
                textBox1.ReadOnly = true;
                textBox1.Text = "-";
            }
            else
            {
                textBox1.ReadOnly = false;
                textBox1.Text = "";
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            textBox2.Text = comboBox1.Text;
            dataGridView1.Rows.Clear();
            selectedScenario = comboBox1.Text;
            string id = "", action = "", parameters = "";
            try
            {
                textBox3.Text = "";
                textBox3.Text = File.ReadAllText(scenarioPath + selectedScenario).Split(new[] { "<description>" }, StringSplitOptions.None)[1].Split(new[] { "</description>" }, StringSplitOptions.None)[0];
            }
            catch { }

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
                        dataGridView1.Rows.Add(id.Replace("\n", ""), action.Replace("\n", ""), parameters.Replace("\n", ""));
                        id = ""; action = ""; parameters = "";
                    }
                }
                if (selectedScenario.Contains(".json"))
                {
                    string nline = line.Replace("{ \"data\" : {", string.Empty);
                    foreach (string row in nline.Split(new[] { "\"}" }, StringSplitOptions.None))
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

        public void makeDescription(string filePath)
        {
            try
            {
                File.Delete(filePath);
            }
            catch { }
            StreamWriter streamWriter = new StreamWriter(filePath);
            streamWriter.Write(textBox3.Text);
            streamWriter.Close();
        }

        public void saveFile(string filePath)
        {

            try
            {
                File.Delete(filePath);
            }
            catch { }
            StreamWriter streamWriter = new StreamWriter(filePath);
            int lastLine = dataGridView1.Rows.Count - 1;
            selectedScenario = filePath.Split('.')[filePath.Split('.').Length - 1];
            if (selectedScenario.Contains("json")) { streamWriter.Write("{ \"data\" : {"); }
            if (selectedScenario.Contains("scenario"))
            {
                streamWriter.Write("<description>\n");
                streamWriter.Write(textBox3.Text + "\n");
                streamWriter.Write("</description>\n");
            }

            for (int i = 0; i < dataGridView1.Rows.Count; i++)
            {
                if (selectedScenario.Contains("scenario"))
                {
                    if (dataGridView1.Rows[i].Cells[0].Value != null && dataGridView1.Rows[i].Cells[1].Value != null && dataGridView1.Rows[i].Cells[2].Value != null)
                    {
                        streamWriter.Write($"<id>{dataGridView1.Rows[i].Cells[0].Value}</id>".Replace("\n", "").Replace("\r", "") + "\n");
                        streamWriter.Write($"\t<action>{dataGridView1.Rows[i].Cells[1].Value}</action>".Replace("\n", "").Replace("\r", "") + "\n");
                        streamWriter.Write($"\t<parameters>{dataGridView1.Rows[i].Cells[2].Value}</parameters>".Replace("\n", "").Replace("\r", "") + "\n");
                    }
                }
                else if (selectedScenario.Contains("json"))
                {
                    if (dataGridView1.Rows[i].Cells[0].Value != null && dataGridView1.Rows[i].Cells[1].Value != null && dataGridView1.Rows[i].Cells[2].Value != null)
                    {
                        streamWriter.Write("\"" + dataGridView1.Rows[i].Cells[0].Value.ToString().Replace("\n", "").Replace("\r", "") + "\" : {");
                        streamWriter.Write("\"action\" : \"" + dataGridView1.Rows[i].Cells[1].Value.ToString().Replace("\n", "").Replace("\r", "") + "\", ");
                        streamWriter.Write("\"parameters\" : \"");
                        foreach (char c in dataGridView1.Rows[i].Cells[2].Value.ToString())
                        {
                            if (Char.IsSymbol(c)) { streamWriter.Write("\\" + c); } else { streamWriter.Write(c); }
                        }
                        streamWriter.Write("\"");
                        if (lastLine - 1 == i) { }
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

        public async void uploadToServer(string filePath, string filename)
        {
            HttpClient httpClient = new HttpClient();
            MultipartFormDataContent form = new MultipartFormDataContent();
            byte[] data = File.ReadAllBytes(filePath);
            form.Add(new StringContent(Environment.UserName), "username");
            form.Add(new ByteArrayContent(data, 0, data.Length), "filename", filename);
            try
            {
                var response = await httpClient.PostAsync("http://host/cgi-bin/gate.py", form);
                string resultContent = await response.Content.ReadAsStringAsync();
            }
            catch { }
        }
        public string adder(string text)
        {
            string firstValue = "", secondValue = "", thirdValue = "";
            text = text.Replace("\n\"", "\"");
            for (int i = 0; i < text.Split('\n').Length; i++)
            {
                if (text.Split('\n')[i].Contains("<id>"))
                    firstValue = text.Split('\n')[i].Replace("<id>", "").Replace("</id>", "").Replace("\n", "");
                if (text.Split('\n')[i].Contains("<action>"))
                    secondValue = text.Split('\n')[i].Replace("<action>", "").Replace("</action>", "").Replace("\n", "");
                if (text.Split('\n')[i].Contains("<parameters>"))
                    thirdValue = text.Split('\n')[i].Replace("<parameters>", "").Replace("</parameters>", "").Replace("\n", "");
                if (firstValue != "" && secondValue != "" && thirdValue != "")
                {
                    dataGridView1.Rows.Add(firstValue, secondValue, thirdValue);
                    firstValue = "";
                    secondValue = "";
                    thirdValue = "";
                }

            }
            return "";
        }
        public string texbox1_add(string text)
        {
            textBox1.Text = text;
            return "";
        }
        private void button2_Click(object sender, EventArgs e)
        {
            bool saved = false;
            if (textBox2.Text == string.Empty)
            {
                MessageBox.Show("Please, input filename!");
            }
            else
            {
                if ((File.Exists(scenarioPath + textBox2.Text)) && saved == false)
                {
                    DialogResult dialog = MessageBox.Show("File already exist! Rewrite?", "Warning", MessageBoxButtons.YesNo, MessageBoxIcon.Warning, MessageBoxDefaultButton.Button1);
                    if (dialog == DialogResult.Yes)
                    {
                        //makeDescription(descriptionPath + textBox2.Text + ".txt");
                        saveFile(scenarioPath + textBox2.Text);
                        //uploadToServer(scenarioPath + textBox2.Text, textBox2.Text);
                        saved = true;
                    }
                    if (dialog == DialogResult.No) { }
                }
                if (textBox2.Text == string.Empty)
                {
                    MessageBox.Show("Please, input filename!", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                if (textBox2.Text != string.Empty)
                {
                    if ((!textBox2.Text.Contains(".scenario") || !textBox2.Text.Contains(".json") && saved == false))
                    {
                        //makeDescription(descriptionPath + textBox2.Text + ".txt");
                        saveFile(scenarioPath + textBox2.Text + ".scenario");
                        //uploadToServer(scenarioPath + textBox2.Text + ".scenario", textBox2.Text + ".scenario");
                        saved = true;
                    }
                }
            }
            MessageBox.Show("Successfully saved!");
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
                try
                {
                    List<string> list = new List<string>();
                    int selectedRowIndex = dataGridView1.SelectedRows[0].Index;
                    var selectedLine = dataGridView1.Rows[dataGridView1.SelectedRows[0].Index];
                    //list.Add(dataGridView1.Rows[selectedRowIndex - 1].Cells[0].Value.ToString());
                    if (dataGridView1.Rows[selectedRowIndex - 1] != null && dataGridView1.Rows[selectedRowIndex - 1].Cells[1].Value != null)
                    {
                        list.Add(dataGridView1.Rows[selectedRowIndex - 1].Cells[1].Value.ToString());
                        list.Add(dataGridView1.Rows[selectedRowIndex - 1].Cells[2].Value.ToString());
                        //dataGridView1.Rows[selectedRowIndex - 1].Cells[0].Value = selectedLine.Cells[0].Value;
                        dataGridView1.Rows[selectedRowIndex - 1].Cells[1].Value = selectedLine.Cells[1].Value;
                        dataGridView1.Rows[selectedRowIndex - 1].Cells[2].Value = selectedLine.Cells[2].Value;
                        //selectedLine.Cells[0].Value = list[0];
                        selectedLine.Cells[1].Value = list[0];
                        selectedLine.Cells[2].Value = list[1];
                        dataGridView1.Refresh();
                        dataGridView1.Rows[selectedRowIndex - 1].Selected = true;
                    }
                }
                catch { }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {

            if (this.dataGridView1.SelectedRows.Count > 0)
            {
                try
                {
                    List<string> list = new List<string>();
                    int selectedRowIndex = dataGridView1.SelectedRows[0].Index;
                    var selectedLine = dataGridView1.Rows[dataGridView1.SelectedRows[0].Index];
                    //list.Add(dataGridView1.Rows[selectedRowIndex + 1].Cells[0].Value.ToString());
                    if (dataGridView1.Rows[selectedRowIndex + 1] != null && dataGridView1.Rows[selectedRowIndex + 1].Cells[1].Value != null)
                    {
                        list.Add(dataGridView1.Rows[selectedRowIndex + 1].Cells[1].Value.ToString());
                        list.Add(dataGridView1.Rows[selectedRowIndex + 1].Cells[2].Value.ToString());
                        //dataGridView1.Rows[selectedRowIndex + 1].Cells[0].Value = selectedLine.Cells[0].Value;
                        dataGridView1.Rows[selectedRowIndex + 1].Cells[1].Value = selectedLine.Cells[1].Value;
                        dataGridView1.Rows[selectedRowIndex + 1].Cells[2].Value = selectedLine.Cells[2].Value;
                        //selectedLine.Cells[0].Value = list[0];
                        selectedLine.Cells[1].Value = list[0];
                        selectedLine.Cells[2].Value = list[1];
                        dataGridView1.Refresh();
                        dataGridView1.Rows[selectedRowIndex + 1].Selected = true;
                    }
                    
                }
                catch{ }
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            try
            {
                //dataGridView1.SelectedCells[0].RowIndex
                dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Selected = true;
                comboBox2.SelectedItem = dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Cells[1].Value;
                textBox1.Text = dataGridView1.Rows[dataGridView1.SelectedCells[0].RowIndex].Cells[2].Value.ToString();
                button1.Text = "Change";
            }
            catch { }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Form2 form2 = new Form2();
            form2.Show();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            dataGridView1.Rows.Clear();
            comboBox1.Text = "";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            nexusTake form = new nexusTake(this);
            form.Show();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            string filename;
            using (OpenFileDialog dialog = new OpenFileDialog())
            {
                dialog.Title = "Import simple lines from txt file";
                dialog.ShowDialog();
                filename = dialog.FileName;
            }
            foreach (string line in File.ReadLines(filename))
            {
                dataGridView1.Rows.Add("*", "Manual", line.Replace("\n", ""));
            }
        }

        private void dataGridView1_CellContentClick_1(object sender, DataGridViewCellEventArgs e)
        {

        }


        private void button11_Click(object sender, EventArgs e)
        {
            if (textBox4.Text == "") { MessageBox.Show("Please, enter hostname"); }
            else if (comboBox1.Text == "") { MessageBox.Show("Please, choose scenario"); }
            else if (textBox5.Text == "") { MessageBox.Show("Please, enter chain name"); }
            else if (textBox4.Text != "" && comboBox1.Text != "")
            {
                if (!new_chain.Contains("["))
                {
                    new_chain += $"[{textBox5.Text}]";
                }
                new_chain += $"{textBox4.Text}->{comboBox1.SelectedItem};";
                label4.Text = new_chain;
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            new_chain = "";
            label4.Text = "";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            string filePath = Directory.GetCurrentDirectory() + "/chains/list.txt";
            var file = File.AppendText(filePath);
            file.WriteLine(new_chain);
            file.Close();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Form3 form3 = new Form3(this);
            form3.Show();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            command_text = textBox1.Text;
        }
    }
}
