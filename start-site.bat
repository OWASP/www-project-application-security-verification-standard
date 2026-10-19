@echo off
setlocal
pushd "%~dp0"
if errorlevel 1 exit /b 1

where ruby >nul 2>&1
if errorlevel 1 (
    echo Ruby is required. Install Ruby 3.3 with Devkit from https://rubyinstaller.org/downloads/
    echo Run the installer's MSYS2 toolchain setup, then open this file again.
    goto :failed
)

where bundle >nul 2>&1
if errorlevel 1 (
    echo Installing Bundler...
    call gem install bundler --no-document
    if errorlevel 1 goto :failed
)

rem Keep downloaded gems in this checkout.
set "BUNDLE_PATH=vendor/bundle"
set "JEKYLL_ENV=development"
call bundle check >nul 2>&1
if errorlevel 1 (
    echo Installing site dependencies. The first run may take a few minutes...
    call bundle install
    if errorlevel 1 goto :failed
)

echo.
echo Starting the ASVS website at http://127.0.0.1:4000/
echo Wait for Jekyll's Server running message, then open that address in your browser.
echo Keep this window open. Press Ctrl+C to stop the server.
echo.
call bundle exec jekyll serve --host 127.0.0.1 --port 4000 --baseurl ""
if errorlevel 1 goto :failed
popd
endlocal
exit /b 0

:failed
echo.
echo Could not start the website. See the error above.
echo If native gem compilation failed, run ridk install to install the Ruby Devkit toolchain.
echo If port 4000 is in use, stop the other server and try again.
pause
popd
endlocal
exit /b 1
