# Hello Rails Docker Container

1. Linux (non-WSL) users only: before the first run, run this on the
   command line:

   ```
   export MYUID=$(id -u)
   export MYGID=$(id -g)
   ```

   After the container runs once, there's no need to do this again.

2. Run the container:

   ```
   docker compose run --service-ports --rm cs362-hellorails bash
   ```

3. Start the [Getting
   Started](https://guides.rubyonrails.org/getting_started.html)
   tutorial at section 3.2.

   Don't worry that we're not at the latest version.

   **NOTE**: if the `rails new store` command fails with a sqlite3
   error, edit the `Gemfile` in the `store/` directory and change the
   `sqlite3` line to be this:

   ```
   gem "sqlite3", "~> 1.7"
   ```

   Then go back and run `rails new store` again, answering `n` for all
   the overwrite prompts.

The `blog` directory gets mapped into the container, so you can access
it with VS Code from outside the container. **All the rails commands
from the tutorial must be run inside the container.**

Be sure to run the server in the container with `rails server -b
0.0.0.0` so you can access `localhost:3000` in your browser from outside
the container.

