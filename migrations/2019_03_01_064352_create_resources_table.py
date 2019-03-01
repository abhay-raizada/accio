from orator.migrations import Migration


class CreateResourcesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('resources') as table:
            table.increments('id')
            table.string('url')
            table.string('name')
            table.integer('user_id')
            table.timestamps()
            table.soft_deletes()
            table.index(['user_id', 'name'])

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
