package stms301;

import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.StringSelection;
import java.awt.datatransfer.Transferable;
import java.awt.datatransfer.UnsupportedFlavorException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.DefaultComboBoxModel;
import javax.swing.SwingWorker;

public class STMSJFrame extends javax.swing.JFrame {

    public STMSJFrame() {
        initComponents();
        //проверим наличие каталога .\TEMP
        File_Exists(".\\TEMP");
        //проверим наличие конфига
        File_Exists(".\\config.txt");
        try {
            Read_Config();
        } catch (IOException ex) {
            Logger.getLogger(STMSJFrame.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        RbuttonGroup = new javax.swing.ButtonGroup();
        PopupMenu_req = new javax.swing.JPopupMenu();
        MenuItem_paste = new javax.swing.JMenuItem();
        jSeparator1 = new javax.swing.JPopupMenu.Separator();
        MenuItem_copy = new javax.swing.JMenuItem();
        Label_req = new javax.swing.JLabel();
        Label_log = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        TextArea_req = new javax.swing.JTextArea();
        jScrollPane2 = new javax.swing.JScrollPane();
        TextArea_log = new javax.swing.JTextArea();
        jPanel1 = new javax.swing.JPanel();
        jCheckBox1 = new javax.swing.JCheckBox();
        jCheckBox2 = new javax.swing.JCheckBox();
        jCheckBox3 = new javax.swing.JCheckBox();
        jCheckBox4 = new javax.swing.JCheckBox();
        jCheckBox5 = new javax.swing.JCheckBox();
        jCheckBox6 = new javax.swing.JCheckBox();
        jCheckBox7 = new javax.swing.JCheckBox();
        jPanel2 = new javax.swing.JPanel();
        RadioButton_import = new javax.swing.JRadioButton();
        RadioButton_copy = new javax.swing.JRadioButton();
        Button_import = new javax.swing.JButton();
        Label_source = new javax.swing.JLabel();
        ComboBox_source_sid = new javax.swing.JComboBox<>();
        ComboBox_target_sid = new javax.swing.JComboBox<>();
        Label_target = new javax.swing.JLabel();
        Progress_bar = new javax.swing.JProgressBar();

        MenuItem_paste.setText("Вставить");
        MenuItem_paste.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                MenuItem_pasteActionPerformed(evt);
            }
        });
        PopupMenu_req.add(MenuItem_paste);
        PopupMenu_req.add(jSeparator1);

        MenuItem_copy.setText("Копировать");
        MenuItem_copy.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                MenuItem_copyActionPerformed(evt);
            }
        });
        PopupMenu_req.add(MenuItem_copy);

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("STMS 3.1");
        setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        setLocationByPlatform(true);
        setResizable(false);

        Label_req.setText("Запросы:");

        Label_log.setText("Журнал выполнения переносов запросов:");

        TextArea_req.setFont(new java.awt.Font("Verdana", 0, 12)); // NOI18N
        TextArea_req.setLineWrap(true);
        TextArea_req.setToolTipText("Каждый деблокированный запрос на новой строке");
        TextArea_req.setWrapStyleWord(true);
        TextArea_req.setComponentPopupMenu(PopupMenu_req);
        jScrollPane1.setViewportView(TextArea_req);

        TextArea_log.setEditable(false);
        TextArea_log.setFont(new java.awt.Font("Verdana", 0, 11)); // NOI18N
        TextArea_log.setLineWrap(true);
        TextArea_log.setText("Импорт запросов осуществляется поочерёдно сверху вниз, несмотря на ошибки. Например, если во втором запросе были ошибки, то всё равно начнёт переноситься третий и т.д. Возможно, лучше переносить по очереди, чтобы отслеживать статусы переносов.\n");
        TextArea_log.setToolTipText("");
        TextArea_log.setWrapStyleWord(true);
        jScrollPane2.setViewportView(TextArea_log);

        jPanel1.setBorder(javax.swing.BorderFactory.createTitledBorder("Опции импорта"));
        jPanel1.setToolTipText("");

        jCheckBox1.setSelected(true);
        jCheckBox1.setText("Оставить запрос на перенос для другого импорта");

        jCheckBox2.setSelected(true);
        jCheckBox2.setText("Ещё раз импортировать запрос на перенос");

        jCheckBox3.setText("Перезапись оригиналов");

        jCheckBox4.setSelected(true);
        jCheckBox4.setText("Перезаписать объекты в неподтверждённых исправлениях");

        jCheckBox5.setText("Игнорировать недопустимый вид");

        jCheckBox6.setText("Игнорировать недопустимый класс таблицы");

        jCheckBox7.setText("Игнорировать предыдущие отношения");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jCheckBox1)
                    .addComponent(jCheckBox2)
                    .addComponent(jCheckBox3)
                    .addComponent(jCheckBox4)
                    .addComponent(jCheckBox5)
                    .addComponent(jCheckBox6)
                    .addComponent(jCheckBox7))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jCheckBox1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jCheckBox2)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jCheckBox3)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jCheckBox4)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jCheckBox5)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jCheckBox6)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jCheckBox7)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        jPanel2.setBorder(javax.swing.BorderFactory.createBevelBorder(javax.swing.border.BevelBorder.RAISED));

        RbuttonGroup.add(RadioButton_import);
        RadioButton_import.setText("Импортировать");
        RadioButton_import.setToolTipText("");

        RbuttonGroup.add(RadioButton_copy);
        RadioButton_copy.setSelected(true);
        RadioButton_copy.setText("Только копировать");
        RadioButton_copy.setToolTipText("и добавить в буфер");

        Button_import.setIcon(new javax.swing.ImageIcon(getClass().getResource("/stms301/favicon.png"))); // NOI18N
        Button_import.setToolTipText("Поехали");
        Button_import.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                Button_importActionPerformed(evt);
            }
        });

        Label_source.setText("Откуда:");

        ComboBox_source_sid.setToolTipText("");

        ComboBox_target_sid.setToolTipText("");

        Label_target.setText("Куда:");

        Progress_bar.setStringPainted(true);

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(Progress_bar, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                            .addComponent(Label_source, javax.swing.GroupLayout.DEFAULT_SIZE, 80, Short.MAX_VALUE)
                            .addComponent(ComboBox_source_sid, 0, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 42, Short.MAX_VALUE)
                        .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(Label_target)
                            .addComponent(ComboBox_target_sid, javax.swing.GroupLayout.PREFERRED_SIZE, 90, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(RadioButton_import)
                            .addComponent(RadioButton_copy)
                            .addComponent(Button_import))
                        .addGap(0, 0, Short.MAX_VALUE)))
                .addContainerGap())
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(Label_source)
                    .addComponent(Label_target))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(ComboBox_source_sid, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(ComboBox_target_sid, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(RadioButton_copy)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(RadioButton_import)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(Button_import, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(Progress_bar, javax.swing.GroupLayout.PREFERRED_SIZE, 24, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(Label_req)
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(Label_log)
                    .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 648, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap())
            .addGroup(layout.createSequentialGroup()
                .addGap(54, 54, 54)
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(27, 27, 27)
                .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(Label_req)
                    .addComponent(Label_log))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 347, Short.MAX_VALUE)
                    .addComponent(jScrollPane2, javax.swing.GroupLayout.DEFAULT_SIZE, 347, Short.MAX_VALUE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 19, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(11, 11, 11))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(23, 23, 23))))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    String source_user = "", source_session = "", source_host = "", source_sid = "", import_Options = "";
    String target_user = "", target_session = "", target_host = "", target_sid = "", target_mndt = "", target_controler = "";
    ArrayList<String> list_config = new ArrayList<>();
    String[] list_sids, req_arr;
    Map< String, String > list_users_hash = new HashMap<  >();
    Map< String, String > list_session_hash = new HashMap<  >();
    Map< String, String > list_hosts_hash = new HashMap<  >();
    Map< String, String > list_controlers_hash = new HashMap<  >();
    Map< String, String > list_mndts_hash = new HashMap<  >();
    
    //проверим наличие файла
    public void File_Exists(String filename) {
        File file = new File(filename);
        if (file.exists() == false) {
            AppendLog("\nВНИМАНИЕ! НЕ ОБНАРУЖЕН " + filename + "\n");
        }
    }
    
    //прочитаем конфиг и заполним раскрывающиеся списки
    public void Read_Config() throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader(".\\config.txt"))) {
            String line = null;
            while ((line = br.readLine()) != null) { //сохраняем каждую строку файла в отдельный элемент массива
                list_config.add(line);
            }
            br.close(); //закрываем файл
        }
        list_sids = new String[list_config.size()]; //массив сидов по количеству строк
        String[] temp_split = new String[list_config.size()];
        for (int i = 0; i < list_config.size(); i++) { //создаём хеш-массивы, где ключом является сид системы
            temp_split = list_config.get(i).split(","); //разбираем строку, используя запятую, как разделитель и сохраняем всё во временный массив
            list_sids[i] = list_sids[i] = temp_split[0]; //сохраняем массив сидов из нулевого элемента временного массива
            list_users_hash.put(list_sids[i].substring(0, 3), temp_split[1]); //сохраняем с ключом-сидом хэш пользователей из первого элемента временного массива
            list_session_hash.put(list_sids[i].substring(0, 3), temp_split[2]);
            list_hosts_hash.put(list_sids[i].substring(0, 3), temp_split[3]);
            list_controlers_hash.put(list_sids[i].substring(0, 3), temp_split[4]);
            list_mndts_hash.put(list_sids[i].substring(0, 3), temp_split[5]);
        }
        ComboBox_source_sid.setModel(new DefaultComboBoxModel(list_sids));
        ComboBox_target_sid.setModel(new DefaultComboBoxModel(list_sids));
    }
    
    //заполним переменные в соответствии с выбранными сидами
    public void Fill_Var() {
        source_sid = ComboBox_source_sid.getSelectedItem().toString().substring(0, 3); //берём три первых символа для исходного сида
        target_sid = ComboBox_target_sid.getSelectedItem().toString().substring(0, 3); //берём три первых символа для целевого сида
        source_user = list_users_hash.get(source_sid);
        source_session = list_session_hash.get(source_sid);
        source_host = list_hosts_hash.get(source_sid);
        target_user = list_users_hash.get(target_sid);
        target_session = list_session_hash.get(target_sid);
        target_host = list_hosts_hash.get(target_sid);
        target_controler = list_controlers_hash.get(target_sid);
        target_mndt = list_mndts_hash.get(target_sid);
        req_arr = TextArea_req.getText().split("\n"); //читаем массив запросов
        Progress_bar.setValue(0);
    }

    private void Button_importActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_Button_importActionPerformed
        
        req_arr = new String[0]; //обнуляем массив запросов
        
        Fill_Var();
        //проверим совпадение исходной системы с целевой
        if (source_sid.equals(target_sid)){
            AppendLog("\nВНИМАНИЕ! ИСХОДНАЯ И ЦЕЛЕВАЯ СИСТЕМЫ СОВПАДАЮТ\n");
            return;
        }
        //проверим на пустоту поле для запросов
        if (TextArea_req.getText().isEmpty()) {
            AppendLog("\nВНИМАНИЕ! НЕ УКАЗАНО НИ ОДНОГО ЗАПРОСА\n");
            return;
        }
        
        for (int i = 0; i < req_arr.length; i++) {
            req_arr[i] = req_arr[i].trim(); //убираем возможные пробелы
            req_arr[i] = req_arr[i].toUpperCase(); //на всякий случай переводим названия запросов в верхний регистр
            if (req_arr[i].length() != 10) { //проверяем названия запросов на длину
                AppendLog("\nВНИМАНИЕ! НАЗВАНИЕ ЗАПРОСА " + req_arr[i] + " НЕ РАВНО 10-ТИ СИМВОЛАМ\n");
                return;
            }
        }
        ImportAction worker = new ImportAction();
        Button_import.setEnabled(false);
        RadioButton_copy.setEnabled(false);
        RadioButton_import.setEnabled(false);
        ComboBox_source_sid.setEnabled(false);
        ComboBox_target_sid.setEnabled(false);
        jCheckBox1.setEnabled(false);
        jCheckBox2.setEnabled(false);
        jCheckBox3.setEnabled(false);
        jCheckBox4.setEnabled(false);
        jCheckBox5.setEnabled(false);
        jCheckBox6.setEnabled(false);
        jCheckBox7.setEnabled(false);
        worker.execute();
    }//GEN-LAST:event_Button_importActionPerformed
    
    //считываем опции импорта
    public void Which_Options() {
        import_Options = " u";
        if (jCheckBox1.isSelected()) { import_Options = import_Options + "0"; }
        if (jCheckBox2.isSelected()) { import_Options = import_Options + "1"; }
        if (jCheckBox3.isSelected()) { import_Options = import_Options + "2"; }
        if (jCheckBox4.isSelected()) { import_Options = import_Options + "3"; }
        if (jCheckBox5.isSelected()) { import_Options = import_Options + "6"; }
        if (jCheckBox6.isSelected()) { import_Options = import_Options + "8"; }
        if (jCheckBox7.isSelected()) { import_Options = import_Options + "9"; }
    }
        
    //вставить запрос из буфера обмена
    private void MenuItem_pasteActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_MenuItem_pasteActionPerformed
        Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
        Transferable clipData = clipboard.getContents(clipboard);
        if (clipData != null) {
            if (clipData.isDataFlavorSupported(DataFlavor.stringFlavor)) {
                String s = null;
                try {
                    s = (String) (clipData.getTransferData(DataFlavor.stringFlavor));
                } catch (UnsupportedFlavorException ex) {
                    Logger.getLogger(STMSJFrame.class.getName()).log(Level.SEVERE, null, ex);
                } catch (IOException ex) {
                    Logger.getLogger(STMSJFrame.class.getName()).log(Level.SEVERE, null, ex);
                }
                TextArea_req.replaceSelection(s);
            }
        }
    }//GEN-LAST:event_MenuItem_pasteActionPerformed
    //скопировать запрос в буфер обмена
    private void MenuItem_copyActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_MenuItem_copyActionPerformed
        String selection = TextArea_req.getSelectedText();
        StringSelection data = new StringSelection(selection);
        Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
        clipboard.setContents(data, data);
    }//GEN-LAST:event_MenuItem_copyActionPerformed

    //запускаем команду на выполнение на удалённом хосте и читаем ответ от него
    public void Connect_Host (String command2exec) {
        String line;
        try {
            Runtime r = Runtime.getRuntime();
            Process p = r.exec(command2exec);
            InputStream stdout = p.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(stdout));
            while ((line = reader.readLine()) != null) {
                AppendLog(line + "\n");
            }
            p.destroy();
        } catch (IOException ex) {
            Logger.getLogger(STMSJFrame.class.getName()).log(Level.SEVERE, null, ex);
        }      
    }
    
    //добавляем строку в лог
    public void AppendLog (String log_text) {
        TextArea_log.append(log_text);
    }

    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(STMSJFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(STMSJFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(STMSJFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(STMSJFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            @Override
            public void run() {
                new STMSJFrame().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton Button_import;
    private javax.swing.JComboBox<String> ComboBox_source_sid;
    private javax.swing.JComboBox<String> ComboBox_target_sid;
    private javax.swing.JLabel Label_log;
    private javax.swing.JLabel Label_req;
    private javax.swing.JLabel Label_source;
    private javax.swing.JLabel Label_target;
    private javax.swing.JMenuItem MenuItem_copy;
    private javax.swing.JMenuItem MenuItem_paste;
    private javax.swing.JPopupMenu PopupMenu_req;
    private javax.swing.JProgressBar Progress_bar;
    private javax.swing.JRadioButton RadioButton_copy;
    private javax.swing.JRadioButton RadioButton_import;
    private javax.swing.ButtonGroup RbuttonGroup;
    private javax.swing.JTextArea TextArea_log;
    private javax.swing.JTextArea TextArea_req;
    private javax.swing.JCheckBox jCheckBox1;
    private javax.swing.JCheckBox jCheckBox2;
    private javax.swing.JCheckBox jCheckBox3;
    private javax.swing.JCheckBox jCheckBox4;
    private javax.swing.JCheckBox jCheckBox5;
    private javax.swing.JCheckBox jCheckBox6;
    private javax.swing.JCheckBox jCheckBox7;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JPopupMenu.Separator jSeparator1;
    // End of variables declaration//GEN-END:variables

public class ImportAction extends SwingWorker<Void, Void> {

    @Override
    protected Void doInBackground() throws Exception {

        String line_req = "", command_CopyR = "", command_CopyK = "", command_CopyD = "", command_Addbuf = "", command_Import = "";
        
        String[] req_file = new String[req_arr.length]; //инициализируем массив запросов без первых трёх символов
        for (int i = 0; i < req_arr.length; i++) {
            req_file[i] = req_arr[i].substring(4); //заполняем массив запросов без первых трёх символов
        }
        for (int i = 0; i < req_arr.length; i++) {
            line_req = line_req + " " + req_arr[i]; //просто запоминаем названия запросов в строку
        }
        Progress_bar.setValue(20);
        AppendLog("КОПИРУЕМ ЗАПРОС(Ы)" + line_req + " ИЗ ИСХОДНОЙ СИСТЕМЫ " + source_sid + " НА ЛОКАЛЬНЫЙ КОМПЬЮТЕР В .\\TEMP\n");
        for (int i = 0; i < req_arr.length; i++) {
            AppendLog(">>pscp.exe -scp -load " + source_session + " " + source_user + "@" + source_host + ":/usr/sap/trans/data/R" + req_file[i] + "." + source_sid + " .\\TEMP\\R" + req_file[i] + "." + source_sid + "\n");
            command_CopyR = "pscp.exe -scp -load " + source_session + " " + source_user + "@" + source_host + ":/usr/sap/trans/data/R" + req_file[i] + "." + source_sid + " .\\TEMP\\R" + req_file[i] + "." + source_sid;
            Connect_Host(command_CopyR);
            AppendLog(">>pscp.exe -scp -load " + source_session + " " + source_user + "@" + source_host + ":/usr/sap/trans/cofiles/K" + req_file[i] + "." + source_sid + " .\\TEMP\\K" + req_file[i] + "." + source_sid + "\n");
            command_CopyK = "pscp.exe -scp -load " + source_session + " " + source_user + "@" + source_host + ":/usr/sap/trans/cofiles/K" + req_file[i] + "." + source_sid + " .\\TEMP\\K" + req_file[i] + "." + source_sid;
            Connect_Host(command_CopyK);
            AppendLog(">>pscp.exe -scp -load " + source_session + " " + source_user + "@" + source_host + ":/usr/sap/trans/data/D" + req_file[i] + "." + source_sid + " .\\TEMP\\D" + req_file[i] + "." + source_sid + "\n");
            command_CopyD = "pscp.exe -scp -load " + source_session + " " + source_user + "@" + source_host + ":/usr/sap/trans/data/D" + req_file[i] + "." + source_sid + " .\\TEMP\\D" + req_file[i] + "." + source_sid;
            Connect_Host(command_CopyD);            
        }
        Progress_bar.setValue(40);
        AppendLog("КОПИРУЕМ ЗАПРОС(Ы)" + line_req + " В ЦЕЛЕВУЮ СИСТЕМУ " + target_sid + " И ДОБАВЛЯЕМ В БУФЕР\n");
        for (int i = 0; i < req_arr.length; i++) {
            AppendLog(">>pscp.exe -scp -load " + target_session + " .\\TEMP\\R" + req_file[i] + "." + source_sid + " " + target_user + "@" + target_host + ":/usr/sap/trans/data/R" + req_file[i] + "." + source_sid + "\n");
            command_CopyR = "pscp.exe -scp -load " + target_session + " .\\TEMP\\R" + req_file[i] + "." + source_sid + " " + target_user + "@" + target_host + ":/usr/sap/trans/data/R" + req_file[i] + "." + source_sid;
            Connect_Host(command_CopyR);
            //добавим права на файл
            command_CopyR = "plink.exe -load " + target_session + " chmod 664 /usr/sap/trans/data/R" + req_file[i] + "." + source_sid;
            Connect_Host(command_CopyR);

            AppendLog(">>pscp.exe -scp -load " + target_session + " .\\TEMP\\K" + req_file[i] + "." + source_sid + " " + target_user + "@" + target_host + ":/usr/sap/trans/cofiles/K" + req_file[i] + "." + source_sid + "\n");
            command_CopyK = "pscp.exe -scp -load " + target_session + " .\\TEMP\\K" + req_file[i] + "." + source_sid + " " + target_user + "@" + target_host + ":/usr/sap/trans/cofiles/K" + req_file[i] + "." + source_sid;
            Connect_Host(command_CopyK);
            //добавим права на файл
            command_CopyK = "plink.exe -load " + target_session + " chmod 664 /usr/sap/trans/cofiles/K" + req_file[i] + "." + source_sid;
            Connect_Host(command_CopyK);
            
            AppendLog(">>pscp.exe -scp -load " + target_session + " .\\TEMP\\D" + req_file[i] + "." + source_sid + " " + target_user + "@" + target_host + ":/usr/sap/trans/data/D" + req_file[i] + "." + source_sid + "\n");
            command_CopyD = "pscp.exe -scp -load " + target_session + " .\\TEMP\\D" + req_file[i] + "." + source_sid + " " + target_user + "@" + target_host + ":/usr/sap/trans/data/D" + req_file[i] + "." + source_sid;
            Connect_Host(command_CopyD);
            //добавим права на файл
            command_CopyD = "plink.exe -load " + target_session + " chmod 664 /usr/sap/trans/data/D" + req_file[i] + "." + source_sid;
            Connect_Host(command_CopyD);            

            AppendLog(">>plink.exe -load " + target_session + " tp addtobuffer " + req_arr[i] + " " + target_sid + " pf=" + target_controler + "\n");
            command_Addbuf = "plink.exe -load " + target_session + " tp addtobuffer " + req_arr[i] + " " + target_sid + " pf=" + target_controler;
            Connect_Host(command_Addbuf);
        }
        Progress_bar.setValue(80);
        if (RadioButton_import.isSelected()) {
            Which_Options();
            AppendLog("ИМПОРТИРУЕМ ЗАПРОС(Ы)" + line_req + " В ЦЕЛЕВУЮ СИСТЕМУ " + target_sid + "\n");
            for (int i = 0; i < req_arr.length; i++) {
                AppendLog(">>plink.exe -load " + target_session + " tp import " + req_arr[i] + " " + target_sid + " client" + target_mndt + import_Options + " pf=" + target_controler + "\n");
                command_Import = "plink.exe -load " + target_session + " tp import " + req_arr[i] + " " + target_sid + " client" + target_mndt + import_Options + " pf=" + target_controler;
                Connect_Host(command_Import);
            }
        }
        Progress_bar.setValue(100);
        Button_import.setEnabled(true);
        RadioButton_copy.setEnabled(true);
        RadioButton_import.setEnabled(true);
        ComboBox_source_sid.setEnabled(true);
        ComboBox_target_sid.setEnabled(true);
        jCheckBox1.setEnabled(true);
        jCheckBox2.setEnabled(true);
        jCheckBox3.setEnabled(true);
        jCheckBox4.setEnabled(true);
        jCheckBox5.setEnabled(true);
        jCheckBox6.setEnabled(true);
        jCheckBox7.setEnabled(true);
        return null;
    }
}

}
