package com.project.readtimespring.Data;

import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
@EnableJpaRepositories
public interface DataRepo extends CrudRepository<GetData, Integer> {


}
