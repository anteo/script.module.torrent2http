script.module.torrent2http
==========================

This add-on is binding to [torrent2http](https://github.com/anteo/torrent2http) client. 
It is bundled with torrent2http binaries for Android ARM, Linux x86/x64/ARM, Windows x86/x64 and Darwin/OSX x64 platforms.
You can download it from my [repository](http://bit.ly/184XKjm)

This add-on can be used to stream media files from torrents without need to download entire files.

Internally, it runs pre-compiled torrent2http client binary, which starts local HTTP server, presenting contents of torrent.
Next, request to HTTP server can be sent to receive list of files or to start streaming of needed file inside of torrent.

Usage
-----

### Get list of files inside torrent ###

Getting list of files inside torrent is straightforward:

    import xbmc 
    from torrent2http import State, Engine, MediaType
    from contextlib import closing

    # Create instance of Engine 
    engine = Engine(uri="...")
    files = []
    # Ensure we'll close engine on exception 
    with closing(engine):
        # Start engine 
        engine.start()
        # Wait until files received 
        while not files and not xbmc.abortRequested:
            # Will list only video files in torrent
            files = engine.list(media_types=[MediaType.VIDEO])
            # Check if there is loading torrent error and raise exception 
            engine.check_torrent_error()
            xbmc.sleep(200)

### Start streaming ###

    import xbmc 
    from torrent2http import State, Engine, MediaType
    from contextlib import closing

    # We can know file_id of needed video file on this step, if no, we'll try to detect one.
    file_id = None
    engine = Engine(uri="...")
    with closing(self.engine):
        # Start engine and instruct torrent2http to begin download first file, 
        # so it can start searching and connecting to peers  
        self.engine.start(file_id or 0)
        while not xbmc.abortRequested:
            sleep(self.SLEEP_DELAY)
            status = self.engine.status()
            self.engine.check_torrent_error(status)
            if status.state in [State.DOWNLOADING, State.FINISHED, State.SEEDING]:
                ready = True
                break

... todo ...