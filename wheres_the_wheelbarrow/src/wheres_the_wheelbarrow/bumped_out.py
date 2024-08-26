	"""

	@agent
	def inventory_management(self) -> Agent:
		return Agent(
			config=self.agents_config['inventory_management'],
			verbose=True,
			llm=llm
		)

	@agent
	def database_developer(self) -> Agent:
		return Agent(
			config=self.agents_config['database_developer'],
			verbose=True,
			tools=[database_start_tool, database_insert_tool, database_retrieval_tool],
			llm=llm
		)

	
""" 	@task
	def inventory_management_task(self) -> Task:
		return Task(
			config=self.tasks_config['inventory_management_task'],
		)

	@task
	def database_management_task(self) -> Task:
		return Task(
			config=self.tasks_config['database_management_task'],
		)

	@task
	def inventory_insert_task(self) -> Task:
		return Task(
			config=self.tasks_config['inventory_insert_task'],
		)

	@task
	def inventory_retrieval_task(self) -> Task:
		return Task(
			config=self.tasks_config['inventory_retrieval_task'],
			human_input=True
		) 



    @agent
    def image_recognizer(self) -> Agent:
        return Agent(
            config=self.agents_config['image_recognizer'],
            verbose=True,
            llm=llm
        ) 
    
    @task
    def image_recognizing_task(self) -> Task:
        return Task(
            config=self.tasks_config['image_recognizing_task']
        ) 


		    @agent
    def image_recognizer(self) -> Agent:
        return Agent(
            config=self.agents_config['image_recognizer'],
            verbose=True,
            llm=llm
        ) 
    
    @task
    def image_recognizing_task(self) -> Task:
        return Task(
            config=self.tasks_config['image_processing_task']
        ) 