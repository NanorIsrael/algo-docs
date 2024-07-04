import Cocoa

class AppDelegate: NSObject, NSApplicationDelegate {
    var window: NSWindow!

    func applicationDidFinishLaunching(_ notification: Notification) {
        let mainScreenFrame = NSScreen.main?.frame ?? NSRect.zero
        let windowSize = NSMakeRect(
            mainScreenFrame.size.width / 4,
            mainScreenFrame.size.height / 4,
            mainScreenFrame.size.width / 2,
            mainScreenFrame.size.height / 2
        )
        
        window = NSWindow(
            contentRect: windowSize,
            styleMask: [.titled, .closable, .resizable, .miniaturizable],
            backing: .buffered,
            defer: false
        )
        window.title = "My Mac App"
        window.makeKeyAndOrderFront(nil)

        let button = NSButton(frame: NSMakeRect(20, 20, 200, 40))
        button.title = "Mount NTFS Drive"
        button.target = self
        button.action = #selector(mountNTFSDrive)
        window.contentView?.addSubview(button)
    }

    @objc func mountNTFSDrive() {
        let script = """
        do shell script "sudo /usr/local/sbin/ntfs-3g /dev/disk2s1 /Volumes/NTFS -o local -o allow_other -o auto_xattr -o auto_cache" with administrator privileges
        """

        var error: NSDictionary?
        if let scriptObject = NSAppleScript(source: script) {
            if let output: NSAppleEventDescriptor = scriptObject.executeAndReturnError(&error) {
                print("Output: \(output.stringValue ?? "")")
            } else if let error = error {
                print("Error: \(error)")
            }
        }
    }
}

let app = NSApplication.shared
let delegate = AppDelegate()
app.delegate = delegate
app.run()
