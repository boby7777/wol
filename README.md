# Wake-on-LAN 程式

這個程式是用Python編寫的Wake-on-LAN（WoL）工具，它可以通過輸入MAC地址來寄送Wake-on-LAN封包，以遠程開啟支援WoL功能的設備。

## 功能

- 寄送Wake-on-LAN封包：使用者可以輸入目標設備的MAC地址，程式將寄送封包以開啟該設備。
- 記錄輸入的資料：程式會記錄使用者輸入的MAC地址，並在下次執行時作為預設值。

## 使用方法

1. 確保你的設備已安裝Python環境（建議使用Python 3）。
2. 下載程式碼文件到你的本地機器。
3. 在終端機或命令提示字元中，進入程式碼所在的目錄。
4. 執行程式：

   ```
   python wol.py
   ```

5. 根據程式提示進行操作：

   - 選擇1：寄送Wake-on-LAN封包。如果沒有預設MAC地址，程式會要求你輸入目標設備的MAC地址，並寄送封包以開啟該設備。傳送封包後將MAC地址設定為預設值。
   - 選擇2：顯示預設MAC地址。如果你先前設定過預設MAC地址，程式將顯示該值。
   - 選擇3：設定預設MAC地址。你可以輸入新的MAC地址，設定為預設值，下次執行程式時將自動載入。
   - 選擇4：離開程式。

## 格式驗證

程式會檢查輸入的MAC地址是否符合正確格式，格式應為`00:11:22:33:44:55`或`00-11-22-33-44-55`。如果輸入的MAC地址格式不正確，程式將顯示錯誤訊息並要求重新輸入。

## 資料儲存

使用者輸入的MAC地址和預設MAC地址會被儲存在`wol_data.json`檔案中。如果該檔案不存在，程式將自動建立該檔案。

## 注意事項

- 程式中的MAC地址格式驗證僅支援以下格式：XX:XX:XX:XX:XX:XX 或 XX-XX-XX-XX-XX-XX，其中X代表16進位數字或英文字母。
- 請確保你的網路環境支援Wake-on-LAN功能，並且目標電腦已正確設定WoL相關設定。
- 目標電腦通常需要在同一個區域網路（LAN）中才能正常工作。

## 授權

此程式以[MIT 授權](LICENSE)釋出，詳細資訊請參閱LICENSE檔案。
