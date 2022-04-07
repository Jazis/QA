using System.IO;
using Renci.SshNet;


namespace MachineManager
{
    internal static class Form2Helpers
    {

        public static string getValueFromConfig(string path, string value)
        {
            string intrestedLine = "";
            try
            {
                foreach (string line in File.ReadAllLines(path))
                {
                    if (line.Split('=')[0].Trim() == "[" + value.ToString().Trim() + "]") { intrestedLine = line.Split('=')[1]; break; }
                }
                if (intrestedLine[0] == ' ') { intrestedLine = intrestedLine.Remove(0, 1); }
            }
            catch { }
            return intrestedLine;
        }
        public static string waitForResponseResultOut(SshCommand sshCmd)
        {
            bool flag = sshCmd.Result.Contains("Complete!");
            return sshCmd.Result;
        }

        public static SftpClient sftpConnect()
        {
            SftpClient sftpClient = new SftpClient(Form2.login.Split('@')[1], Form2.login.Split('@')[0], Form2.password);
            //SftpClient client = new SftpClient(Form2.login.Split(new char[]
            //{
            //    '@'
            //})[1], 22, Form2.password.Split(new char[]
            //{
            //    '@'
            //})[0], Form2.password);
            sftpClient.Connect();
            return sftpClient;
        }
    }
}