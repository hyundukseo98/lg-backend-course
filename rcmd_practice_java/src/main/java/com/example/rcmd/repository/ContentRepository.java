package com.example.rcmd.repository;

import com.example.rcmd.models.entity.Content;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ContentRepository extends JpaRepository<Content, Integer> {
    @Query("SELECT m FROM Content m ORDER BY m.createdAt DESC")
    List<Content> findLatestMovies();

}