using System;
using System.Windows.Forms;

namespace ScenarioMaker
{
    public partial class Form3 : Form
    {
        public static int counter = 0;
        public static string preset = "param_";
        Form1 form1;
        public Form3(Form1 frm1)
        {
            InitializeComponent();
            this.form1 = frm1;
        }

        private void Form3_Load(object sender, EventArgs e)
        {
            textBox2.Text = "{" + $"{preset}{counter}" + "}";
            textBox1.Text = Form1.command_text;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox1.SelectedText = textBox2.Text;
            counter++;
            textBox2.Text = "{" + $"{preset}{counter}" + "}";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            form1.texbox1_add(textBox1.Text);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
