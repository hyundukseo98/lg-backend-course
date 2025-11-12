package com.example.rcmd.repository;

import com.example.rcmd.models.entity.Content;
import com.example.rcmd.models.entity.RcmdUserContent;
import com.example.rcmd.models.entity.RcmdUserContentId;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface RecommendationRepository extends JpaRepository<RcmdUserContent, RcmdUserContentId> {
    
    @Query("SELECT m FROM Content m JOIN RcmdUserContent r ON m.contentId = r.contentId WHERE r.userId = :userId")
    List<Content> findUserRecommendations(@Param("userId") Integer userId);
}