using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Threading;
using System.Windows.Forms;


namespace MachineManager
{
    public partial class Form1 : Form
    {
        public static string configPath;
        public static ComboBox comboBox = new ComboBox();
        public static string selectedConfig;
        public static Form2 form2 = new Form2();

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        { 

        }

        private void buttonOk_Click(object sender, EventArgs e)
        {
            selectedConfig = comboBox.SelectedItem.ToString();
            form2.Show();
            this.Hide();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.button1.Visible = false;
            this.button2.Visible = false;
            this.ClientSize = new System.Drawing.Size(400, 80);
            Button buttonOk = new Button();
            buttonOk.Visible = true;
            buttonOk.Text = "OK";
            buttonOk.Location = new Point(10, 20);
            buttonOk.Height = 30;
            buttonOk.Width = 50;
            this.Controls.Add(buttonOk);
            comboBox.Visible = true;
            comboBox.Location = new Point(70, 20);
            comboBox.Height = 30;
            comboBox.Width = 300;
            this.Controls.Add(comboBox);
            buttonOk.Click += new EventHandler(buttonOk_Click);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            configPath = Directory.GetCurrentDirectory() + "\\configs\\";
            foreach (var filename in Directory.GetFiles(configPath))
            {
                if (filename.Contains(".conf"))
                    comboBox.Items.Add(filename.Split(new[] { "\\" },StringSplitOptions.None)[filename.Split(new[] { "\\" }, StringSplitOptions.None).Length-1]);
            }
        }
    }
}
